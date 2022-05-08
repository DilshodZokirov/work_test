from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from account.models import Employee


def has_group(groups=None, raise_exception=False):
    if not groups or len(groups) == 0:
        raise Exception("You did not provide any group")

    def group_required(func):
        def wrapper(request, *args, **kwargs):
            if groups and not check_group(groups, request):
                if raise_exception:
                    raise PermissionDenied
                return HttpResponse("You are not authorized see this page")
            else:
                return func(request, *args, **kwargs)

        return wrapper

    return group_required


def check_group(groups: list, request) -> bool:
    for group in groups:
        if Employee.objects.filter(user_type=group, user=request.user.id).exists():
            return True
    return False

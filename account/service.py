from django.contrib.auth.models import User
from django.db import transaction

from account.forms import RegisterForm
from account.models import Employee


@transaction.atomic()
def create_user(form: RegisterForm):
    data = form.data
    user = User()
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.username = data.get('username')
    user.email = data.get('email')
    user.set_password(raw_password=data.get('password'))
    user.is_active = 1
    user.is_superuser = 0
    user.save()
    employee = Employee()
    employee.user_type = data.get("user_type")
    employee.phone = data.get('phone')
    employee.profile_image = form.files.get('profile_image')
    employee.user = user
    employee.save()


def username_exists(username: str) -> bool:
    return User.objects.filter(username=username).exists()


def email_exists(email: str) -> bool:
    return User.objects.filter(email=email).exists()

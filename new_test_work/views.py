from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from account.models import Employee
from core.models import Category, CategoryUser


@login_required
def home_view(request):
    if request.user.employee.user_type == "STUDENT":
        course = Category.objects.all()
        context = {'courses': course}
        return render(request, 'student.html', context=context)
    elif request.user.employee.user_type == "MENTOR":
        category = Category.objects.filter(created_by=request.user.id)
        context = {"category": category}
        return render(request, 'mentor.html', context=context)
    elif request.user.employee.user_type == "ADMIN":
        category = Category.objects.all()
        user = Employee.objects.filter(user_type="MENTOR_OR_STUDENT").count()
        context = {"category": category, 'users': user}
        return render(request, 'admin.html', context=context)
    else:
        all_category = Category.objects.all()
        context = {'all_category': all_category}
        return render(request, 'other.html', context=context)

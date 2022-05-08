import logging

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from account.models import Employee
from core.forms import CategoryForm, CategoryUpdateForm
from core.models import Category, CategoryUser
from subject_lesson.models import SubjectLesson


class CategoryView(TemplateView):
    template_name = 'category_create.html'

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                title = data.get('title')
                description = data.get('description')
                category = Category(title=title, description=description, created_by=request.user)
                category.save()
                return redirect('home')
            except Exception as e:
                logging.error(e)
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


def category_update(request, cat_id):
    org = get_object_or_404(Category, id=cat_id)
    form = CategoryUpdateForm(instance=org)
    if request.method == "POST":
        form = CategoryUpdateForm(request.POST, instance=org)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'category_edit.html', context)


def category_detail(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    category_user = CategoryUser.objects.filter(category_id=category.id, user_id=request.user.id)
    category_user_count = CategoryUser.objects.filter(category_id=category.id)
    user_count = category_user_count.count()
    subject_lesson = SubjectLesson.objects.filter(category_id=category.id)
    return render(request, 'category_detail.html',
                  {
                      "category": category,
                      'subject_lesson': subject_lesson,
                      'user_count': user_count,
                      'category_user': category_user
                  })


def category_delete_page(request, cat_id: int):
    category = Category.objects.get(id=cat_id)
    return render(request, 'category_delete.html', {'category': category})


def category_delete(request, cat_id: int):
    category = Category.objects.get(id=cat_id)
    category.delete()
    return redirect('home')


def create_student_category(request, pk):
    category = Category.objects.get(id=pk)
    users, created = CategoryUser.objects.get_or_create(
        user_id=request.user.id,
        category_id=category
    )
    try:
        users.save()
    except User.DoesNotExist:
        return HttpResponseRedirect(redirect('category:detail_category', pk))
    return redirect('category:detail_category', pk)


def student_category(request):
    users = CategoryUser.objects.filter(user_id=request.user.id)
    context = {'users': users}
    return render(request, 'user_category.html', context=context)


def admin_checked_mentor_or_student(request):
    users = Employee.objects.filter(user_type="MENTOR_OR_STUDENT")
    context = {'all_users': users}
    return render(request, 'admin_checked.html', context=context)


def update_user_type_mentor(request, user_id):
    first_user = User.objects.get(id=user_id)
    phone = first_user.employee.phone
    profile_pic = first_user.employee.profile_image
    if first_user:
        first_user.employee.delete()
    user, update = Employee.objects.get_or_create(
        user=first_user,
        phone=phone,
        profile_image=profile_pic,
        user_type="MENTOR")
    try:
        user.save()
        messages.success(request, 'Role muvoffaqiyatli  o\'zgardi')
        return HttpResponseRedirect(reverse('home'))
    except User.DoesNotExist:
        messages.success(request, 'Uzr sizda xatolik bor!!')
        return redirect('home')


def update_user_type_student(request, user_id):
    first_user = User.objects.get(id=user_id)
    phone = first_user.employee.phone
    profile_pic = first_user.employee.profile_image
    if first_user:
        first_user.employee.delete()
    user, update = Employee.objects.get_or_create(
        user=first_user,
        phone=phone,
        profile_image=profile_pic,
        user_type="STUDENT")
    try:
        user.save()
        messages.success(request, 'Role muvoffaqiyatli  o\'zgardi')
        return HttpResponseRedirect(reverse('home'))
    except User.DoesNotExist:
        messages.success(request, 'Uzr sizda xatolik bor!!')
        return redirect('home')

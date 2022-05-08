import logging

from django.shortcuts import render, redirect, get_object_or_404
from core.models import Category
from .models import SubjectLesson
from .forms import SubjectLessonForm, SubjectLessonUpdateForm


def create_subject(request, pk):
    category = Category.objects.get(id=pk)
    form = SubjectLessonForm(request.POST, request.FILES)
    if form.is_valid():
        try:
            data = form.cleaned_data
            title = data.get('title')
            description = data.get('description')
            video = form.files.get('video')
            project = SubjectLesson(title=title, description=description, video=video, category_id=category.pk)
            project.save()
            return redirect('home')
        except Exception as e:
            logging.error(e)
            return render(request, 'create_subject.html', {'form': form})
    else:
        return render(request, 'create_subject.html', {'form': form})


def subject_lesson_update(request, pk):
    sub = get_object_or_404(SubjectLesson, id=pk)
    form = SubjectLessonUpdateForm(instance=sub)
    if request.method == "POST":
        form = SubjectLessonUpdateForm(request.POST, request.FILES, instance=sub)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'subject_edit.html', context)


def subject_detail(request, cat_id, sub_id):
    category = get_object_or_404(Category, id=cat_id)
    subject_lesson = SubjectLesson.objects.get(id=sub_id, category_id=cat_id)
    return render(request, 'subject_detail.html', {
        'category': category,
        'subject_lesson': subject_lesson
    }
                  )


def subject_delete_page(request, pk: int, cat_id):
    category = Category.objects.get(id=cat_id)
    subject = SubjectLesson.objects.get(id=pk)
    return render(request, 'subject_delete.html', {'subject': subject, 'category': category})


def subject_delete(request, pk: int, cat_id):
    subject = SubjectLesson.objects.get(id=pk)
    subject.delete()
    return redirect('category:detail_category', cat_id)

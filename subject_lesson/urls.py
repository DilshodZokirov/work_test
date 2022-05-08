from django.urls import path
from .views import create_subject, subject_lesson_update,subject_delete, subject_delete_page, subject_detail

app_name = "subject"
urlpatterns = [
    path('create_subject/<int:pk>', create_subject, name="create_subject"),
    path('update_subject/<int:pk>', subject_lesson_update, name="update_subject"),
    path('delete_subject/<int:pk>/<int:cat_id>', subject_delete, name="delete_subject"),
    path('delete_subject_page/<int:pk>/<cat_id>', subject_delete_page, name="delete_subject_page"),
    path('detail_subject/<int:cat_id>/<int:sub_id>', subject_detail, name="detail_subject"),

]

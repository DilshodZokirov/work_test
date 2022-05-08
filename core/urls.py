from django.urls import path
from .views import CategoryView, category_update, category_detail, category_delete_page, category_delete, \
    create_student_category, student_category, admin_checked_mentor_or_student, update_user_type_mentor, \
    update_user_type_student

app_name = 'category'
urlpatterns = [
    path('category_create/', CategoryView.as_view(), name='create_category'),
    path('category_update/<str:cat_id>/', category_update, name='update_category'),
    path('category_detail/<str:cat_id>/', category_detail, name='detail_category'),
    path('category_delete_page/<str:cat_id>/', category_delete_page, name='delete_category_page'),
    path('category_delete/<str:cat_id>/', category_delete, name='delete_category'),
    path('create_student_category/<str:pk>/', create_student_category, name='create_category_user'),
    path('my_category/', student_category, name="my_category"),
    path('admin_user_checked/', admin_checked_mentor_or_student, name="admin_checked"),
    path('user_type_mentor/<int:user_id>', update_user_type_mentor, name="user_type_mentor"),
    path('user_type_student/<int:user_id>', update_user_type_student, name="user_type_student"),
]

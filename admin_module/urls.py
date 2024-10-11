from django.urls import path

from student_module.views import delete_user, add_user, update_user
from . import views
from .views import main, search_student

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student/', views.search_student, name='search_student'),

    path('student/find/', views.find_student, name='find_student'),

    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('users/add/', add_user, name='add_user'),
    path('users/update/<int:user_id>/', update_user, name='update_user'),
    path('', main, name='admin_main'),
]

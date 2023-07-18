from django.urls import path
from .views import *

urlpatterns = [
    path('api/students/', student_list, name='student-list'),
    path('api/staff/', staff_list, name='staff-list'),
    path('api/courses/', course_list, name='course-list'),
    path('api/staff/', create_staff, name='create-staff'),
    path('api/staff/<int:staff_id>/', staff_detail, name='staff-detail'),
    
]


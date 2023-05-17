from api.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',student_api,name='student_api'),
    path('student_api/<int:pk>',student_api,name='student_api')
    
]

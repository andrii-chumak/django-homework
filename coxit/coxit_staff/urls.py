from django.contrib import admin
from django.urls import path, re_path
from .views import worker_dashboard, hire_worker

urlpatterns = [
    path('dashboard', worker_dashboard, name='workers_dashboard'),
    re_path(r'^(?P<position>\w+)/$', worker_dashboard, name='workers_position'),
    path('hire-worker', hire_worker, name='hire_worker'),
]
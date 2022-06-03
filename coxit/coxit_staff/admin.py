from django.contrib import admin
from .models import CoxitWorker, Position, WorkerPosition


# Register your models here.
admin.site.register(CoxitWorker)
admin.site.register(Position)
admin.site.register(WorkerPosition)
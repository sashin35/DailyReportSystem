from django.contrib import admin
from .models import DailyReportModel, EmployeeModel

# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(DailyReportModel)

from django.contrib import admin

from employees.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')

admin.site.register(Employee, EmployeeAdmin)

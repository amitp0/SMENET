from django.contrib import admin

# Register your models here.
from .models import Company,Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display=('comp_id','username','company_location','company_domain','phone_no','email')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('emp_id','emp_name','company_id','domain','ready_to_relocate','current_loc','resume_link','notice_period','laidoffdate')

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
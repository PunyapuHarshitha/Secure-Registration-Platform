# admin.py
from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'person_mobile_no', 'adhar_no', 'institute_name', 'institute_govt_reg_no', 'institute_website')
    search_fields = ['person_name', 'institute_name', 'institute_govt_reg_no']
    fieldsets = (
        (None, {
            'fields': ('person_name', 'person_mobile_no', 'adhar_no')
        }),
        ('File Uploads', {
            'fields': ('adhar_front', 'adhar_back', 'institute_reg_copy')
        }),
        ('Institute Information', {
            'fields': ('institute_name', 'institute_govt_reg_no', 'institute_website')
        }),
        ('Password', {
            'fields': ('password', 'confirm_password')
        })
    )

admin.site.register(Registration, RegistrationAdmin)

from django.contrib import admin
from insurance.models import *


class SubjectInsuranceAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return f"{obj.name} {obj.surname}"

    full_name.short_description = 'Full Name'

    list_display = [
        'id',
        'full_name',
        'email',
        'phone_number',
        'adress',
    ]
    list_display_links = ['full_name']


admin.site.register(InsuranceSubject, SubjectInsuranceAdmin)

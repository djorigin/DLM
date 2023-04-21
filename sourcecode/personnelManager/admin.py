from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'first_name', 'middle_name', 'last_name')
        }),
        ('Personal Information', {
            'fields': ('phone', 'gender', 'date_of_birth', 'age', 'profile_photo')
        }),
        ('Government Information', {
            'fields': ('tax_file_number', 'licence_number')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )

from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'contact_name', 'contact_address', 
        'contact_number', 'contact_email'
        )
admin.site.register(Contact, ContactAdmin)

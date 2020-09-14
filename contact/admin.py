from django.contrib import admin

from .models import ContactInfo


class ContactInfoAdmin(admin.ModelAdmin):
    fields = ['email', 'full_name', 'subject', 'message']
    list_display = ('email', 'subject')


admin.site.register(ContactInfo, ContactInfoAdmin)

from django.contrib import admin
from main.models import Contact1
# Register your models here.
class ContactAdmin1(admin.ModelAdmin):
    list_display = ['email','name','address','message','sent_at']

    list_filter = ['sent_at']

    search_fields =  ['email','name','address','message','sent_at']

    # list_editable = ['address']
admin.site.register(Contact1, ContactAdmin1)
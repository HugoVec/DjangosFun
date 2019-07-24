from django.contrib import admin
from .models import DKs, Client


class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'last_name', 'age', 'salary', 'photo']
    list_display = ['name', 'last_name', 'age', 'salary']
    list_filter = ['name', 'last_name', 'age', 'salary']
    search_fields = ['last_name', 'age']


# Register your models here.
admin.site.register(DKs)
admin.site.register(Client, ClientAdmin)

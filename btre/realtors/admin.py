from django.contrib import admin
from .models import Realtors


# Register your models here.
@admin.register(Realtors)
class RealtorAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name', 'email', 'hire_date')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

#admin.site.register(Realtors)
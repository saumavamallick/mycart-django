from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # populated_fields = {'slug':('name',)} took care of this in save method already
    list_display = ('name','slug')

admin.site.register(Category, CategoryAdmin)

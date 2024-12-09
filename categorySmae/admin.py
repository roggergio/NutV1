from django.contrib import admin
from .models import CategorySmae

# Register your models here.
class CategorySmaeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = 'category_name','slug'
admin.site.register(CategorySmae, CategorySmaeAdmin)
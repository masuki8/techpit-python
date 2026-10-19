from django.contrib import admin
from blog.models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
   list_display=('id','title', 'postdate','category')

class CategoryAdmin(admin.ModelAdmin):
   list_display=('id','category_name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

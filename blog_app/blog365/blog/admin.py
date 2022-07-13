import imp
from django.contrib import admin
from .models import Category, Post

#username : blog365
#password : blog365

#to use js in admin


#costomitation for admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','add_date') 
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','add_date') #to display all this values in admin panel
    search_fields = ('title',) #To use search functionality of ModelAdmin class which is built-in class
    list_filter = ('cat',) #to filter posts by category at admin side
    list_per_page = 10

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

# Register your models here.
admin.site.register(Category, CategoryAdmin) # to register model in admin.py
admin.site.register(Post, PostAdmin)

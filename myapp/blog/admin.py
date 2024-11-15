from django.contrib import admin
from .models import Post,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # this class is used to customizee the admin page 
    list_display=('title','content') # this only show the title and content field
    search_fields=('title','content') # this is used to search the title and content
    list_filter = ('category',) # this fiters the fields based on category 

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
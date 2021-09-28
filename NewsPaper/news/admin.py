from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'dateCreation', 'title', 'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)

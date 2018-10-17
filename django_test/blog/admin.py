from django.contrib import admin
from .models import Post, User

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time', 'change_time', 'views']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)

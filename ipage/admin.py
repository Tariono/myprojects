from django.contrib import admin
from ipage.models import Post, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)

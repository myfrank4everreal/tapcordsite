from django.contrib import admin
from .models import BlogPost, Comment


# for CKEditor
from django.db import models
from ckeditor.widgets import CKEditorWidget

class BlogPostFormAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


admin.site.register(BlogPost, BlogPostFormAdmin)
admin.site.register(Comment)
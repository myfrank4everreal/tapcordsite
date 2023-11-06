from django.contrib import admin


from .models import Gallery
from .models import Category
from .models import NewsLetterMember

admin.site.register(Gallery)
admin.site.register(Category)
admin.site.register(NewsLetterMember)

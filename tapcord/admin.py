from django.contrib import admin


from .models import Gallery
from .models import Category

admin.site.register(Gallery)
admin.site.register(Category)
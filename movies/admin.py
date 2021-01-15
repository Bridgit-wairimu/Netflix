from django.contrib import admin
from .models import Image,Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('images',)

admin.site.register(Image)
admin.site.register(Category)

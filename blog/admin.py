

# Register your models here.
from django.contrib import admin
from .models import MyUser,Article,Category

admin.site.register(MyUser)
admin.site.register(Article)
admin.site.register(Category)
from django.contrib import admin

# Register your models here.
from .models import Writer,Publisher,Category

admin.site.register(Writer)
admin.site.register(Publisher)
admin.site.register(Category)
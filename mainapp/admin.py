from django.contrib import admin

# Register your models here.
from mainapp.models import *

admin.site.register(Category)
admin.site.register(Meals)

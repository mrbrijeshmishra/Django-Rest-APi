from django.contrib import admin
from .models import product

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ("id","name","desc","price","qty")

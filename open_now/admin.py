from django.contrib import admin

from .models import Business, Measurement

# Register your models here.

admin.site.register(Business)
admin.site.register(Measurement)

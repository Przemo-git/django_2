from django.contrib import admin

# Register your models here.
from .models import Owner, Apartment

admin.site.register(Owner)
admin.site.register(Apartment)
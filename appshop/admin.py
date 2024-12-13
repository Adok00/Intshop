from django.contrib import admin

# Register your models here.

from .models import Brend, Marka, AKP, Color, Car

admin.site.register(Brend)
admin.site.register(Marka)
admin.site.register(AKP)
admin.site.register(Color)
admin.site.register(Car)
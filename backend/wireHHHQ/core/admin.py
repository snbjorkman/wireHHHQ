from django.contrib import admin
from .models import Color, Brand, WireType, Location, Project, WireSku, WireBox, WireUsage

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(WireType)
admin.site.register(Location)
admin.site.register(Project)
admin.site.register(WireSku)
admin.site.register(WireBox)
admin.site.register(WireUsage)

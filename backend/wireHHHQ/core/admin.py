from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path
from .models import Color, Brand, WireType, Location, Project, WireSku, WireBox, WireUsage
from core.views import pull_dtools_projects


def run_dtools_proj_update(request):
    pull_dtools_projects()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["color_desc"]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["brand_desc"]

@admin.register(WireType)
class WireTypeAdmin(admin.ModelAdmin):
    list_display = ["wire_type_desc"]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["location_desc"]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["project_name", "client_name"]
    change_list_template = "admin/core/projects_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run-dtools-proj-update/', self.admin_site.admin_view(run_dtools_proj_update), name='run-dtools-proj-update'),
        ]
        return custom_urls + urls


@admin.register(WireSku)
class WireSkuAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WireSku._meta.fields]

@admin.register(WireBox)
class WireBoxAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WireBox._meta.fields]

@admin.register(WireUsage)
class WireUsageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WireUsage._meta.fields]



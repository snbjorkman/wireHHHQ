from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path
from .models import Color, Brand, WireType, Location, Project, WireSku, WireBox, WireUsage
from core.views import pull_dtools_projects, pull_notion_wiretypes, pull_notion_wireboxes


def run_dtools_proj_update(request):
    pull_dtools_projects()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))



#register these next three
def run_wiretypes_update(request):
    pull_notion_wiretypes()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))


def run_wirebox_update(request):
    pull_notion_wireboxes()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))


#def run_wireusage_update(request):
#    pull_notion_wireusages()
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))



@admin.action(description="Compute Cost per Foot")
def get_cost_per_foot(modeladmin, request, queryset):
    for obj in queryset:
        obj.get_unit_price()



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
    actions = [get_cost_per_foot]
    change_list_template = "admin/core/wiretypes_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run-wiretypes-update/', self.admin_site.admin_view(run_wiretypes_update), name='run-wiretypes-update'),
        ]
        return custom_urls + urls

@admin.register(WireBox)
class WireBoxAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WireBox._meta.fields]
    change_list_template = "admin/core/wireboxes_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run-wirebox-update/', self.admin_site.admin_view(run_wirebox_update), name='run-wirebox-update'),
        ]
        return custom_urls + urls

@admin.register(WireUsage)
class WireUsageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WireUsage._meta.fields]




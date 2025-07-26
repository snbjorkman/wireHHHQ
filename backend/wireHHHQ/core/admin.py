from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import path
from .models import Color, Brand, WireType, Location, Project, WireSku, WireBox, WireUsage
from core.views import pull_dtools_projects, pull_notion_wiretypes


def run_dtools_proj_update(request):
    pull_dtools_projects()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))


def run_wiretypes_update(request):
    pull_notion_wiretypes()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))


@admin.action(description="Compute Cost per Foot")
def get_cost_per_foot(modeladmin, request, queryset):
    for obj in queryset:
        obj.get_unit_price()


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["color_desc"]

    def save_model(self, request, obj, form, change):        
        if not change and Color.objects.filter(color_desc__iexact=form.cleaned_data['color_desc']).exists():
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Color name already exists", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)
        


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["brand_desc"]

    def save_model(self, request, obj, form, change):        
        if not change and Brand.objects.filter(brand_desc__iexact=form.cleaned_data['brand_desc']).exists():
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Brand name already exists", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)

@admin.register(WireType)
class WireTypeAdmin(admin.ModelAdmin):
    list_display = ["wire_type_desc"]

    def save_model(self, request, obj, form, change):        
        if not change and WireType.objects.filter(wire_type_desc__iexact=form.cleaned_data['wire_type_desc']).exists():
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Wire Type already exists", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["location_desc"]

    def save_model(self, request, obj, form, change):        
        if not change and Location.objects.filter(location_desc__iexact=form.cleaned_data['location_desc']).exists():
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Location already exists", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["project_name", "client_name"]
    change_list_template = "admin/core/projects_change_list.html"

    def save_model(self, request, obj, form, change):        
        if not change and Project.objects.filter(project_name__iexact=form.cleaned_data['project_name']).exists():
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Project name already exists", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)

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

    def save_model(self, request, obj, form, change):        
        if not change and WireSku.objects.filter(sku__iexact=form.cleaned_data['sku']).exists():
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Wire sku already exists", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run-wiretypes-update/', self.admin_site.admin_view(run_wiretypes_update), name='run-wiretypes-update'),
        ]
        return custom_urls + urls

@admin.register(WireBox)
class WireBoxAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WireBox._meta.fields]
   
    def save_model(self, request, obj, form, change):        
        if not change and WireBox.objects.filter(wire_box_id__iexact=form.cleaned_data['wire_box_id']).exists():
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Wire box already exists", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)
    

@admin.register(WireUsage)
class WireUsageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WireUsage._meta.fields]
    def save_model(self, request, obj, form, change):
        #check for duplicates 
        #make sure starting wire is greater than ending wire
        #gonna have to change some things up with this one!

        #the date cannot be the same as
        if not change and (form.cleaned_data['start_feet']<form.cleaned_data['end_feet']):
            self._skip_save = True  
        else:
            self._skip_save = False
            super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, '_skip_save', False):
            self.message_user(request, "Error saving wire usage... make sure the starting feet is greater than the ending feet", messages.ERROR)
            return redirect(request.path)  
        return super().response_add(request, obj, post_url_continue)




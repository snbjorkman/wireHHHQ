from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/colors/", views.ColorList.as_view(), name="color_list"),
    path("api/brands/", views.BrandList.as_view(), name="brand_list"),
    path("api/wiretypes/", views.WireTypeList.as_view(), name="wiretype_list"),
    path("api/locations/", views.LocationList.as_view(), name="location_list"),
    path("api/projects/", views.ProjectList.as_view(), name="project_list"),
    path("api/wireskus/", views.WireSkuList.as_view(), name="wiresku_list"),
    path("api/wireboxes/", views.WireBoxList.as_view(), name="wirebox_list"),
    path("api/wireusages/", views.WireUsageList.as_view(), name="wireusage_list"),
]



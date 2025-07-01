from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Color, Brand, WireType, Location, Project, WireSku, WireBox, WireUsage
from .serializers import (
    ColorSerializer, BrandSerializer, WireTypeSerializer, LocationSerializer,
    ProjectSerializer, WireSkuSerializer, WireBoxSerializer, WireUsageSerializer
)
import requests
import json


def index(request):
    return HttpResponse("Hello, world.")



def pull_dtools_projects():
    print("entered dtool api pull function")
    url = "https://dtcloudapi.d-tools.cloud/api/v1/Projects/GetProjects?includeTotalCount=true"
    headers = {
        "X-API-Key": "REPLACE WITH ACTUAL KEY FROM DTOOLS", 
        "Authorization": "Basic RFRDbG91ZEFQSVVzZXI6MyNRdVkrMkR1QCV3Kk15JTU8Yi1aZzlV"
    }
    params = {
        "includeTotalCount": "true"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print(response.text)
        update_projects(response.text)
        
    else:
        print("Request failed with error code: ") 
        print(response)
        


def update_projects(data): 
    
    loads = json.loads(data)

    #for each project, if it does not exist in the DB, add it to the DB.
    for i in loads["projects"]:
        if not Project.objects.filter(project_name=i["name"]):
            Project.objects.create(project_name=i["name"], client_name=i["clientName"])
        




class ColorList(APIView):
    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

class BrandList(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

class WireTypeList(APIView):
    def get(self, request):
        wiretypes = WireType.objects.all()
        serializer = WireTypeSerializer(wiretypes, many=True)
        return Response(serializer.data)

class LocationList(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class WireSkuList(APIView):
    def get(self, request):
        wireskus = WireSku.objects.all()
        serializer = WireSkuSerializer(wireskus, many=True)
        return Response(serializer.data)

class WireBoxList(APIView):
    def get(self, request):
        wireboxes = WireBox.objects.all()
        serializer = WireBoxSerializer(wireboxes, many=True)
        return Response(serializer.data)

class WireUsageList(APIView):
    def get(self, request):
        wireusages = WireUsage.objects.all()
        serializer = WireUsageSerializer(wireusages, many=True)
        return Response(serializer.data)


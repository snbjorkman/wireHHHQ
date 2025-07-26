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
from dotenv import load_dotenv
import os

load_dotenv()


def index(request):
    return HttpResponse("Hello, world.")



def pull_dtools_projects():
    url = "https://dtcloudapi.d-tools.cloud/api/v1/Projects/GetProjects?includeTotalCount=true"
    headers = {
        "X-API-Key": os.getenv("DTOOLS_API_KEY"), 
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

    for i in loads["projects"]:
        if not Project.objects.filter(project_name=i["name"]):
            Project.objects.create(project_name=i["name"], client_name=i["clientName"])
        


def pull_notion_wiretypes():
    url = "https://api.notion.com/v1/databases/16d217799b5580a6b228c28a8cdaa799/query"
    headers = {
        "Authorization": os.getenv("NOTION_API_KEY"),
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers)


    if response.status_code == 200:
        print(response.text)
        update_wiretypes(response.text)
        
    else:
        print("Request failed with error code: ") 
        print(response)




def update_wiretypes(data):
    loads = json.loads(data)


    for i in loads["results"][1:]:
        props = i["properties"]
        sku = props["SKU"]["title"][0]["plain_text"]
        brand = props["Brand"]["rich_text"][0]["plain_text"]
        description = props["Description"]["rich_text"][0]["plain_text"]
        color = props["Color"]["select"]["name"]
        feet = props["Feet"]["number"]
        wire_type = props["Wire Type"]["select"]["name"]
        price = props["Typical Price"]["number"]



        if not (sku == None or feet == None or price == None):
            if not Color.objects.filter(color_desc=color).exists():
                Color.objects.create(color_desc=color)

            if not WireType.objects.filter(wire_type_desc=wire_type).exists():
                WireType.objects.create(wire_type_desc=wire_type)

            if not Brand.objects.filter(brand_desc=brand).exists():
                Brand.objects.create(brand_desc=brand)

            if not WireSku.objects.filter(sku=sku).exists():
                WireSku.objects.create(sku=sku, sku_desc=description, wire_type_id=WireType.objects.get(wire_type_desc=wire_type), brand_id=Brand.objects.get(brand_desc=brand), color_id=Color.objects.get(color_desc=color), feet=feet, typical_cost=price)
                WireSku.objects.get(sku=sku).get_unit_price()





# the below classes might end up not being necessary at all

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


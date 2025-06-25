from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Color, Brand, WireType, Location, Project, WireSku, WireBox, WireUsage
from .serializers import (
    ColorSerializer, BrandSerializer, WireTypeSerializer, LocationSerializer,
    ProjectSerializer, WireSkuSerializer, WireBoxSerializer, WireUsageSerializer
)


def index(request):
    return HttpResponse("Hello, world.")


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


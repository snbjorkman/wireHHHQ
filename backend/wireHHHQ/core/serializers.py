from rest_framework import serializers
from .models import Color, Brand, WireType, Location, Project, WireSku, WireBox, WireUsage

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class WireTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WireType
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class WireSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = WireSku
        fields = '__all__'

class WireBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = WireBox
        fields = '__all__'

class WireUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WireUsage
        fields = '__all__'
from django.db import models
import uuid

class Color(models.Model):
    color_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color_desc = models.CharField(max_length=30)


class Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_desc = models.CharField(max_length=30)


class WireType(models.Model):
    wire_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wire_type_desc = models.CharField(max_length=30)


class Location(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_desc = models.CharField(max_length=30)


class Project(models.Model):
    project_name = models.CharField(max_length=200, primary_key=True, default="PROJECT NAME NOT PROVIDED")
    client_name = models.CharField(max_length = 200, default="CLIENT NAME NOT PROVIDED")


class WireSku(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    wire_type_id = models.ForeignKey(WireType, on_delete=models.SET_DEFAULT, default="TYPE UNASSIGNED")
    brand_id = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default="BRAND UNASSIGNED")
    color_id = models.ForeignKey(Color, on_delete=models.SET_DEFAULT, default="COLOR UNASSIGNED")
    feet = models.IntegerField()
    typical_cost = models.FloatField()
    cost_per_foot = models.FloatField() #this will be computed in the view, maybe in a js function, not in the model.
    

class WireBox(models.Model):
    wire_box_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.ForeignKey(WireSku, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, default = "Warehouse")
    purchase_cost = models.IntegerField()
    purchase_date = models.DateField()
    disposed_date = models.DateField(null=True)
    disposed_feet_rem = models.DateField(null=True)


class WireUsage(models.Model):
    wire_usage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wire_box_id = models.ForeignKey(WireBox, on_delete=models.SET_DEFAULT, default = "BOX UNASSIGNED")
    start_feet = models.IntegerField()
    end_feet = models.IntegerField()
    date_used = models.DateField()
    project_id = models.ForeignKey(Project, on_delete=models.SET_DEFAULT, default = "PROJECT UNASSIGNED") 
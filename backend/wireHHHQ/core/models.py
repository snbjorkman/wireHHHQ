from django.db import models

class Color(models.Model):
    color_id = models.CharField(max_length=30, primary_key=True)
    color_desc = models.CharField(max_length=30)


class Brand(models.Model):
    brand_id = models.CharField(max_length=30, primary_key=True)
    brand_desc = models.CharField(max_length=30)


class WireType(models.Model):
    wire_type_id = models.CharField(max_length=30, primary_key=True)
    wire_type_desc = models.CharField(max_length=30)


class Location(models.Model):
    location_id = models.CharField(max_length=30, primary_key=True)
    location_desc = models.CharField(max_length=30)


class Project(models.Model):
    project_id = models.CharField(max_length=30, primary_key=True)
    subdivision = models.CharField(max_length = 30) #may have a separate table for this that is updated with api
    lot_block = models.CharField(max_length = 30)
    client = models.CharField(max_length = 30)


class WireSku(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    wire_type_id = models.ForeignKey(WireType)
    brand_id = models.ForeignKey(Brand)
    color_id = models.ForeignKey(Color)
    feet = models.IntegerField()
    typical_cost = models.FloatField()
    cost_per_foot = models.FloatField() #this will be computed in the view, maybe in a js function, not in the model.
    

class WireBox(models.Model):
    wire_box_id = models.CharField(max_length=30, primary_key=True)
    sku = models.ForeignKey(WireSku)
    location_id = models.ForeignKey(Location)
    purchase_cost = models.IntegerField()
    purchase_date = models.DateField()
    disposed_date = models.DateField(null=True)
    disposed_feet_rem = models.DateField(null=True)


class WireUsage(models.Model):
    wire_usage_id = models.CharField(max_length=30, primary_key=True)
    wire_box_id = models.ForeignKey(WireBox)
    start_feet = models.IntegerField()
    end_feet = models.IntegerField()
    date_used = models.DateField()
    project_id = models.ForeignKey(Project)
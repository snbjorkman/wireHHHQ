from django.db import models
import uuid

class Color(models.Model):
    color_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color_desc = models.CharField(max_length=30)

    def __str__(self):
        return self.color_desc


class Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_desc = models.CharField(max_length=30)

    def __str__(self):
        return self.brand_desc


class WireType(models.Model):
    wire_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wire_type_desc = models.CharField(max_length=30)

    def __str__(self):
        return self.wire_type_desc

class Location(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_desc = models.CharField(max_length=30)

    def __str__(self):
        return self.location_desc


class Project(models.Model):
    project_name = models.CharField(max_length=200, primary_key=True, default="PROJECT NAME NOT PROVIDED")
    client_name = models.CharField(max_length = 200, default="CLIENT NAME NOT PROVIDED")

    def __str__(self):
        return self.project_name


class WireSku(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    sku_desc = models.CharField(max_length=50, default="DESCRIPTION NOT GIVEN")
    wire_type_id = models.ForeignKey(WireType, on_delete=models.SET_DEFAULT, default="TYPE UNASSIGNED")
    brand_id = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default="BRAND UNASSIGNED")
    color_id = models.ForeignKey(Color, on_delete=models.SET_DEFAULT, default="COLOR UNASSIGNED")
    feet = models.IntegerField()
    typical_cost = models.FloatField()
    cost_per_foot = models.FloatField(blank=True, null=True) 
 
    def get_unit_price(self):
        self.cost_per_foot = self.typical_cost/self.feet
        self.save()


    def __str__(self):
        return self.sku



class WireBox(models.Model):
    wire_box_id = models.CharField(max_length=50, primary_key=True)
    sku = models.ForeignKey(WireSku, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, default = "shelf")
    purchase_cost = models.IntegerField(null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    disposed_date = models.DateField(null=True, blank=True)
    disposed_feet_rem = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.wire_box_id


class WireUsage(models.Model):
    wire_usage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wire_box_id = models.ForeignKey(WireBox, on_delete=models.SET_DEFAULT, default = "BOX UNASSIGNED")
    start_feet = models.IntegerField()
    end_feet = models.IntegerField()
    date_used = models.DateField()
    project_id = models.ForeignKey(Project, on_delete=models.SET_DEFAULT, default = "PROJECT UNASSIGNED") 

    def __str__(self):
        return self.wire_usage_id
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#from django.contrib.gis.db import models
#Seasons in a list are sorted and kept in  a variable seasons
seasons=sorted(["summer","winter","rainy","monsoon"])
seasons=((item,item) for item in seasons)
crop=sorted(["paddy","cotton","maize","turmeric","groundnut","sugarcane","plain"])
crop=((item,item) for item in crop)
#Crops in a list are sorted and kept in  a variable crp
crp=sorted(["paddy","cotton","maize","turmeric","groundnut","sugarcane","plain"])
crp=((item,item) for item in crp)

#A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
# model defines a house_hold, which has a lat,lon,mon_income,links of image
#Each field takes a certain set of field-specific arguments. For example, CharField (and its subclasses) require a max_length argument which specifies the size of the VARCHAR database field used to store the data.
class house_hold(models.Model):
	#maximum digits allowed and no of digits after points as decimal points
	lat=models.DecimalField(max_digits=15, decimal_places=6)
	lon=models.DecimalField(max_digits=15, decimal_places=6)
	#The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object       	is created.	
	mon_income=models.IntegerField(default=0)
	links=models.CharField(default="gfdxgh", max_length=50)
	def __unicode__(self):#Unicode method returns the field which we want instead of returning all fields[Here house_hold mostly depends on house_id]
		return '%s'%(self.id)

#model defines a persons_info, which has a house_id,name,gender,DOB
#If you don’t specify primary_key=True for any fields in your model, Django will automatically add an IntegerField to hold the primary key, so you don’t need to set primary_key=True on any of your fields unless you want to override the default primary-key behavior.
class persons_info(models.Model):
	house_id = models.ForeignKey(house_hold,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	gender=models.CharField(max_length=2)
	DOB=models.DateField(null=True)#If True, Django will store empty values as NULL in the database. Default is False
	def __unicode__(self):
		return '%s'%(self.name)
#Model defines a farm info which has a house_id,area
class farm_info(models.Model):
	house_id = models.ForeignKey(house_hold,on_delete=models.CASCADE)
	#lat=models.DecimalField(max_digits=15, decimal_places=6)
	#lon=models.DecimalField(max_digits=15, decimal_places=6)
	area=models.DecimalField(max_digits=6, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.id)
# The foreign key is defined in a second table, but it refers to the primary key or a unique key in the first table.
#Model defines a farm locations which has farmid,sequence no,lat,lon
class farm_location(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	sequence_no=models.IntegerField(default=0)
	lat=models.DecimalField(max_digits=15, decimal_places=6)
	lon=models.DecimalField(max_digits=15, decimal_places=6)
	def __unicode__(self):
		return '%s'%(self.farm_id)

#Model defines crops which has farmid,crop and crop area
class crops(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	crop=models.CharField(choices=crp,default="paddy", max_length=20)
	crop_area=models.IntegerField(default=0)
	def __unicode__(self):
		return '%s'%(self.farm_id)
#Model defines a season information which has farmid,season,crop,area	
class season_info(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	season=models.CharField(choices=seasons,default="summer", max_length=20)
	crop=models.CharField(choices=crop,default="paddy", max_length=20)
	area=models.DecimalField(max_digits=6, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.farm_id)

#Model defines a well information which has farmid,lat,lon,depth,Avg water yield
class well_info(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	lat=models.DecimalField(max_digits=15, decimal_places=6)
	lon=models.DecimalField(max_digits=15, decimal_places=6)
	depth_in_meters=models.DecimalField(max_digits=6, decimal_places=2)
	Avg_wateryield=models.DecimalField(max_digits=8, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.id)


#Model defines a well observations which has wellid,depth in meters,date of observation,water yield
class well_observation(models.Model):
	well_id = models.ForeignKey(well_info,on_delete=models.CASCADE)
	depth_in_meters=models.DecimalField(max_digits=6, decimal_places=2)
	date_of_observation=models.DateTimeField(null=True)
	wateryield=models.DecimalField(max_digits=8, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.well_id)


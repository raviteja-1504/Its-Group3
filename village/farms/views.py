# -*- coding: utf-8 -*-
#Import the required modules
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from farms.models import *
#Import  serializers
from farms.serializers import *

from django.shortcuts import render

#we get the variable name which was mentioned in urls.py.
def data(request,name):
	#print "sdjfnhjk"
	#print name
	#We are using GET method for security.
	if request.method=='GET':		
		if name=='houselist':#If name is houslist then it enters inside if condition
			household = house_hold.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer = householdserializer(household, many=True)#calls household serializer in serializers
			return JsonResponse(serializer.data, safe=False)#Returns Jsonresponse
		if name=='members':
			persons = persons_info.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer = personsinfoserializer(persons, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='farmlist':
			farms = farm_info.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer = farminfoserializer(farms, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='farmpoints':
			shapes = farm_location.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer = farmlocationserializer(shapes, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='croplist':
			crp = crops.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer =cropserializer(crp, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='seasonlist':
			crop = season_info.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer = seasoninfoserializer(crop, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='welllist':
			well = well_info.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer = wellinfoserializer(well, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='wellobservations':
			observations = well_observation.objects.all()#The QuerySet returned by all() describes all objects in the database table
			serializer = wellobservationserializer(observations, many=True)
			return JsonResponse(serializer.data, safe=False)





# -*- coding: utf-8 -*-
from django.http import HttpResponse
import requests
from django.shortcuts import render
#Import Json
import json
def farm(request):
	r = requests.get('http://127.0.0.1:8000/farms/farmpoints')#Get the data in the url by using request method.Something like below
#[{"id": 3, "lat": "13.520000", "lon": "79.990400", "mon_income": 45000, "links": "https://image.ibb.co/dA1CDw/3.jpg"}, {"id": 1, "lat": "13.520000", "lon": "79.990000", "mon_income": 36000, "links": "https://image.ibb.co/j2xxfb/1.png"}, {"id": 2, "lat": "13.520400", "lon": "79.990000", "mon_income": 15000, "links": "https://image.ibb.co/df0Hfb/2.png"}]
	a = requests.get('http://127.0.0.1:8000/farms/farmlist')
	cr = requests.get('http://127.0.0.1:8000/farms/croplist')
	cr=cr.json()#Convert into Json
	a=a.json()
	j = r.json()
	#Initialize empty lists
	farm_id=[]
	farm_ids=[]
	house_id=[]
	area = []
	lat=[[]]#Double list like  2d matrix
	lon=[[]]
	l1=[]
	l2=[]
	cr1=[]
	cr2=[]
	q=1
	crpl=[[]]
	crpa=[[]]
	fid=[]



	q=2
	#Loop through the Json data contained in variable j
	for k in j:
		if q==2:#In k['farm_id'] farm_id is key and k['farm_id'] returns value for that key 
			farm_id.append(k['farm_id'])#Append farm_id to list farm_id
			l1.append(float(k['lat']))#Append lat to list l1  
			l2.append(float(k['lon']))#Append lon to list l2
			q=3
		else:
			if k['farm_id'] in farm_id:
				l1.append(float(k['lat']))
				l2.append(float(k['lon']))
			else:
				lat.append(l1)
				lon.append(l2)
				farm_id.append(k['farm_id'])
				l1=[]
				l2=[]
				l1.append(float(k['lat']))
				l2.append(float(k['lon']))
	lat.append(l1)#Append list l1 to lat
	lon.append(l2)#Append list l2 to lon
	lat.remove([])#Empty  the list
	lon.remove([])#Empty the list
	print lat
	print lon

	for k in cr:
		#print "sdfh"
		if q==1:
			fid.append(k['farm_id'])
			#print k['farm_id']
			cr1.append(str(k['crop']))
			cr2.append(int(k['crop_area']))
			q=2
		else:
			#print fid
			if k['farm_id'] in fid:
				cr1.append(str(k['crop']))
				cr2.append(int(k['crop_area']))
			else:	
				#print "sdfhsbdfhbsdfbsdjfbjh"
				crpl.append(cr1)
				crpa.append(cr2)
				#print crpl
				#print crpa
				fid.append(k['farm_id'])
				#print k['farm_id']
				cr1=[]
				cr2=[]
				cr1.append(str(k['crop']))
				cr2.append(int(k['crop_area']))
	#Appending to lists	
	crpl.append(cr1)
	crpa.append(cr2)
	#Emptying lists
	crpl.remove([])
	crpa.remove([])
	crpl.remove([])
	crpa.remove([])
	print crpl
	print crpa
	alt=[[]]
	print lat[0]
	for i in range(len(lat)):
		pk=[]
		print i
		a1=reduce(lambda x,y:x+y,lat[i])/len(lat[i])#Calculate the average of latitudes using reduce 
		print a1
		pk.append(a1)#Append to list pk
		b1=reduce(lambda x,y:x+y,lon[i])/len(lon[i])#Calculate the average of longitudes using reduce 
		pk.append(b1)#Append to list pk  
		print pk
		alt.append(pk)
	alt.remove([])#Empty the list
	print alt
	final=[[]]
	for v in range(len(alt)):
		fin=alt[v]+crpa[v]#Add two lists using + operator
		final.append(fin)
	final.remove([])
	print final
	for h in a:
		farm_ids.append(h['id'])#Append id to farm_ids
		house_id.append(h['house_id'])
		area.append(float(h['area']))
	print farm_ids
	print area
	print house_id
	h_id=[]
	for c in farm_id:
		ind=farm_ids.index(c)#Index
		h_id.append(house_id[ind])
	print farm_id
	#Put all the data(lat,lom,farm_id,area,h_id,crpl,crpa,final into their respectives variables)
	context={'lat':lat,'lon':lon,'farm_id':farm_id,'area':area,'h_id':h_id,'crpl':crpl,'crpa':crpa,'final':final}		
	return render(request, 'maps/farm.html', context)#Send this context to maps/farms.html using render




def house(request):
	#Get the data in the url by using request method
	r=requests.get('http://127.0.0.1:8000/farms/houselist')
	a=requests.get('http://127.0.0.1:8000/farms/members')
	j=r.json()
	a=a.json()
	house_id=[]
	lat=[]
	lon=[]
	mi=[]
	ml=[]
	links=[]
	for k in j:
		lk=""
		house_id.append(k['id'])
		lat.append(float(k['lat']))
		lon.append(float(k['lon']))
		mi.append(k['mon_income'])
		lk='<img src="'+str(k['links'])+'">'#Image link
		print lk
		links.append(lk)

	person_names={}
	person_dob={}
	print links
	for k in a:
		#Append  name of particular person belonging to particular house_id
		if k['house_id'] in person_names:
			person_names[k['house_id']].append(str(k['name']))
		else:
			person_names[k['house_id']]=[str(k['name'])]
	for k in a:
		#Append  dob of particular person belonging to particular house_id
		if k['house_id'] in person_dob:
			person_dob[k['house_id']].append(str(k['DOB']))
		else:
			person_dob[k['house_id']]=[str(k['DOB'])]
	info=[]
	st=''
	for s in house_id:
		m=person_names[s]
		print m
		g=len(m)#Contains number of members in particular house
		ml.append(g)
		n=person_dob[s]
		for v in range(len(m)):
			st=st+str(m[v])+' DOB : '+n[v]+'\n'#Append name and dob eg:Name:Ravi,DOB:1997-09-09
		info.append(st)
		st=''#Empty the string
		#print house_id
		#print info[0]
	print ml
	print type(links[0])
	#Put all the data(lat,lon,house_id,mi,info,ml,links into their respectives variables)	
	context={'lat':lat,'lon':lon,'house_id':house_id,'mi':mi,'info':info,'ml':ml,'links':links}
	return render(request, 'maps/house.html', context)#Send this context to maps/house.html using render









def well(request):
	#Get the data in the url by using request method
	r = requests.get('http://127.0.0.1:8000/farms/farmpoints')
	a=requests.get('http://127.0.0.1:8000/farms/welllist')
	#convert into json	
	a=a.json()
	j = r.json()
	farm_id=[]
	lat=[[]]
	lon=[[]]
	l1=[]
	l2=[]
	lat1=[]
	lon1=[]
	depth=[]
	well_id=[]
	avg_yield=[]
	q=1
	f_id=[]
	for k in j:
		if q==1:
			farm_id.append(k['farm_id'])
			l1.append(float(k['lat']))
			l2.append(float(k['lon']))
			q=2
		else:
			if k['farm_id'] in farm_id:
				l1.append(float(k['lat']))
				l2.append(float(k['lon']))
			else:
				lat.append(l1)
				lon.append(l2)
				farm_id.append(k['farm_id'])
				l1=[]
				l2=[]
				l1.append(float(k['lat']))
				l2.append(float(k['lon']))
	lat.append(l1)
	lon.append(l2)
	lat.remove([])
	lon.remove([])
	for k in a:
		f_id.append(k['farm_id'])
		well_id.append(k['id'])
		lat1.append(float(k['lat']))
		lon1.append(float(k['lon']))
		depth.append(float(k['depth_in_meters']))
		avg_yield.append(float(k['Avg_wateryield']))
	farmid=sorted(farm_id)
	#Put all the data(lat,lon,farm_id,f_id,..etc into their respectives variables)	
	context={'lat':lat,'lon':lon,'farm_id':farm_id,'f_id':f_id,'lat1':lat1,'lon1':lon1,'depth':depth,'avg_yield':avg_yield,'well_id':well_id}		
	return render(request, 'maps/well.html', context)#Send this context to maps/house.html using render








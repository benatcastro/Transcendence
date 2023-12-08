from django.shortcuts import render
from django.http import JsonResponse
import json
from random import randint

# Create your views here.

users = []
casuals = []

def makeResponse():
	basic = '{}'
	casual = json.loads(basic)
	newList = {"Users": users}
	casual.update(newList)
	return JsonResponse(casual)

def index(request):
	id = request.GET.get('mode')
	if (id == "casual"):
		value = randint(1000, 9999)
		print (value)
		if not users.__contains__(value):
			users.append(value)
			makeResponse()
			return JsonResponse({"user": value})
		
	# id = request.GET.get('user')
	# if (id == None):
	# 	return makeResponse()
	# users.append(id)


	# i = 0
	# while 1:
	# 	if users[i] == id:
	# 		continue
	# 	if (i >= len(users)):
	# 		i = 0
	# 	if users[i] != id:
	# 		basic = '{}'
	# 		casual = json.loads(basic)
	# 		newList = {"name": users[i]}
	# 		casual.update(newList)
	# 		return JsonResponse(casual)

	return makeResponse()

def delete():
	users.clear()
	return makeResponse()

def search(request):
	i = 0
	while 1:
		if users[i] != int(request.GET.get('user')):
			return JsonResponse({"rival": users[i]})
		i = i + 1
		if i + 1 > len(users):
			i = 0
		print(f"loop {i}")
	return makeResponse()

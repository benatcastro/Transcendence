from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from random import randint

# Create your views here.

casuals = []
rankeds = []

def makeResponse():
	basic = '{}'
	json_response = json.loads(basic)
	newList = {"Users": casuals}
	json_response.update(newList)
	return JsonResponse(json_response)

def index(request):
	id = request.GET.get('mode')
	if (id == "casual"):
		value = randint(1000, 9999)
		print (value)
		if not casuals.__contains__(value):
			casuals.append(value)
		return JsonResponse({"user": value})

	return makeResponse()

def deleteAll(request):
	casuals.clear()
	return redirect("http://localhost:8000/matchmaking/")

def delete(request):
	id = request.GET.get('mode')
	if (id == "casual"):
		print ("DELETE")
		casuals.remove(int(request.GET.get('user')))
	return makeResponse()

def search(request):
	i = 0
	while 1:
		if casuals[i] != int(request.GET.get('user')):
			return JsonResponse({"rival": casuals[i]})
		i = i + 1
		if i + 1 > len(casuals):
			i = 0
	return makeResponse()

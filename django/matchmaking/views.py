from django.shortcuts import redirect
from django.http import JsonResponse
from random import randint

casual_ids = []
ranked_ids = []

def make_response():
	response = {"Casual_ids": casual_ids, "Ranked_ids": ranked_ids}
	return JsonResponse(response)

def show(request):
	return make_response()

def create(request):
	mode = request.GET.get('mode')
	user_id = 0
	if mode == "ranked":
		user_id = request.GET.get('user')
		if user_id not in ranked_ids:
			ranked_ids.append(user_id)
	if mode == "casual":
		user_id = randint(1000, 9999) if request.GET.get('user') is None else int(request.GET.get('user'))
		if len(casual_ids) == 0 or user_id not in casual_ids:
			casual_ids.append(user_id)
	return JsonResponse({"user": user_id})

def search(request):
	if len(casual_ids) == 0 or int(request.GET.get('user')) not in casual_ids:
		create(request)
	while True:
		for i in casual_ids:
			if i != int(request.GET.get('user')):
				return JsonResponse({"rival": i})

def delete(request):
	#TODO: preguntar a Ander si quiere que se borre el usuario si ya se ha encontrado un rival o si quiere que se mantenga hasta quedar AFK en la partida
	print("------------------DELETE------------------")
	mode = request.GET.get('mode')
	print(mode)
	if mode == 'casual' and int(request.GET.get('user')) in casual_ids:
		casual_ids.remove(int(request.GET.get('user')))
	return make_response()

def clear(request):
	casual_ids.clear()
	return redirect("http://localhost:8000/matchmaking/")

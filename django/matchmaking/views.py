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
    user_id = request.GET.get('user') if mode == "ranked" else request.GET.get('user') or str(randint(1000, 9999))
    ids = casual_ids if mode == 'casual' else ranked_ids

    if len(ids) == 0 or user_id not in ids:
        ids.append(user_id)
    return JsonResponse({"user": user_id})


def search(request):
    user_id = str(request.GET.get('user'))
    mode = request.GET.get('mode')
    ids = casual_ids if mode == 'casual' else ranked_ids

    if len(ids) == 0 or user_id not in ids:
        create(request)
    # TODO: This can completely hang the server with enough time: should we tell the puteros to use websockets with Django?
    while True:
        if mode == 'casual':
            rival = next((i for i in ids if i != user_id), None)
            if rival:
                return JsonResponse({"rival": rival})
        else:
            # TODO: algoritmo de búsqueda de partida ranked
            pass


def delete(request):
    # TODO: preguntar a Ander si quiere que se borre el usuario si ya se ha encontrado un rival o si quiere que se
    #  mantenga hasta quedar AFK en la partida
    user_id = str(request.GET.get('user'))
    mode = request.GET.get('mode')
    ids = casual_ids if mode == 'casual' else ranked_ids

    if user_id in ids:
        ids.remove(user_id)
    return make_response()


def clear(request):
    casual_ids.clear()
    ranked_ids.clear()
    return redirect("http://localhost:8000/matchmaking/")

from django.shortcuts import redirect
from django.http import JsonResponse
from random import randint

casual_ids = []
ranked_ids = []

GenericNames1 = ["Gatita", "Capitan", "Tiburon", "Humano", "Alienigena", "Boss", "Dragon", "Watashi wa", "Mamut"]
GenericNames2 = ["Generico", "Sexy", "Badass", "Basado", "Magica", "Heteronormativo", "Ancestral", "Destroyer", "Fuerte"]
GenericNames3 = ["69", "XD", "10/10", "Lvl100", "Amateur", "Facha", "Random", "CSM", "Legendario", "Andy String", "test"]


def make_response():
    response = {"Casual_ids": casual_ids, "Ranked_ids": ranked_ids}
    return JsonResponse(response)


def show(request):
    return make_response()


def create(request):
    mode = request.GET.get('mode')
    user_id = request.GET.get('user') if mode == "ranked" else request.GET.get('user') or GenericNames1[randint(0, len(GenericNames1))] + GenericNames2[randint(0, len(GenericNames2))] + GenericNames3[randint(0, len(GenericNames3))]#str(randint(1000, 9999))
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

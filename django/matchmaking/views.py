from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from random import randint
import os, environ
import json


env = environ.Env()
environ.Env.read_env()
GenericNames1 = [ "Gatita", "Capitan", "Tiburon", "Humano", "Alien", "Boss", "Dragon", "YoSoy", "Mamut", "Ander", "Andy", "Aingeru", "Beniat", "Tonio" ]
GenericNames2 = [ "Legendario", "Lvl100", "Amateur", "Facha", "69", "XD", "Generico", "Sexy", "Badass", "Basado", "Magica", "Heteronormativo", "Ancestral", "Destroyer", "Fuerte" ]

casual_ids = []
ranked_ids = []


def make_response():
    response = {"Casual_ids": casual_ids, "Ranked_ids": ranked_ids}
    return JsonResponse(response)


def show(request):
    return make_response()


def create(request):
    mode = request.GET.get('mode')
    user_id = request.GET.get('user') if mode == "ranked" else request.GET.get('user') or str(GenericNames1[randint(0, len(GenericNames1) - 1)] + GenericNames2[randint(0, len(GenericNames2) - 1)])
    #ids = casual_ids if mode == 'casual' else ranked_ids

    if mode == "casual":
        if len(casual_ids) == 0 or user_id not in casual_ids:
            casual_ids.append(user_id)
    return JsonResponse({"user": user_id})

@csrf_exempt
def search(request):
    if request.method == "GET":
        return
    body = json.loads(request.body.decode('utf-8'))
    print(body)
    user_id = body['user']
    mode = body['mode']
    print("\n\n", user_id, "\n\n", mode, "\n\n")

    #mode = request.POST.get('mode')
    ids = casual_ids if mode == 'casual' else ranked_ids

    print("\n\n", casual_ids, "\n\n")
    if len(ids) == 0 or user_id not in ids:
        create(request)
    # TODO: This can completely hang the server with enough time: should we tell the puteros to use websockets with Django?
    while True:
        if mode == 'casual':
            rival = next((i for i in ids if i != user_id), None)
            if rival:
                room = ""
                if rival > user_id:
                    room = rival + "_" + user_id
                else:
                    room = user_id + "_" + rival
                return JsonResponse({"rival": rival, "room": room})
        else:
            # TODO: algoritmo de búsqueda de partida ranked
            pass


def delete(request):
    # TODO: preguntar a Ander si quiere que se borre el usuario si ya se ha encontrado un rival o si quiere que se
    #  mantenga hasta quedar AFK en la partida
    user_id = str(request.GET.get('user'))
    if user_id in casual_ids:
        casual_ids.remove(user_id)
    return JsonResponse({"ok": "ok"})


def clear(request):
    casual_ids.clear()
    ranked_ids.clear()
    return redirect("https://" + env('IP_BACKEND') + "/1024/matchmaking/")

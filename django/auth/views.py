import logging

import environ
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
import environ
import requests

# Env setup
env = environ.Env()
environ.Env.read_env()


# Exception used when the 42 api fails
# needed for simpler error handling
class ExternalApiError(Exception):
    def __init__(self, status_code, message="", function="undefined"):
        self.status_code = status_code
        self.message = message
        self.function = function
        super().__init__(message)


# Given a dictionary with the key values of the params formats them into a valid string
def format_query_params(params):
    params_string = "?"

    for index, (key, value) in enumerate(params.items()):
        # avoids adding the & char at the first param
        if index != 0:
            params_string += "&"
        params_string += key + "=" + value

    return params_string


# First step into the 42 auth workflow, redirects to the page were the users will enter their 42 credentials
def get_redirect_url():
    url = 'https://api.intra.42.fr/oauth/authorize'

    params = {
        "client_id": env('FT_API_UID'),
        "redirect_uri": env('FT_API_REDIRECT'),
        "response_type": "code",
        'scope': 'public',
    }

    return url + format_query_params(params)


# Posts the users code into the 42 api and retrieves the access token
def retrieve_access_token(code):
    url = 'https://api.intra.42.fr/oauth/token'
    params = {
        "client_id": env('FT_API_UID'),
        "client_secret": env('FT_API_SECRET'),
        "redirect_uri": env('FT_API_REDIRECT'),
        "grant_type": "authorization_code",
        "code": code,
    }

    response = requests.post(url + format_query_params(params))

    if response.status_code == 200:
        # Find the access token into the response body
        # if there is no value for the key "access_token" throws ExternalApiError
        data = response.json()
        token = data.get("access_token", "error")
        return token if token != "error" else None
    else:
        raise ExternalApiError(message=response.json(), status_code=response.status_code, function=retrieve_access_token.__name__)


# Given the access token gets the users data from the api
def get_user_from_api(access_token):
    url = 'https://api.intra.42.fr/v2/me'
    headers = {"Authorization": "Bearer " + access_token}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        email = data.get("email", "error")
        username = data.get("login", "error")
        user = {
            "email": email,
            "username": username
        }
        print(user)
        return user
    else:
        raise ExternalApiError(message=response.json(), status_code=response.status_code, function=get_user_from_api.__name__)


# Entry point for 42 auth handling
def ft_auth(request):
    if request.method == "GET":
        return redirect(get_redirect_url())

    if request.method == "POST":
        try:
            access_token = retrieve_access_token(request.GET.get("code"))
            user = get_user_from_api(access_token)
            return JsonResponse(user)
        except ExternalApiError as e:
            logging.error("External Api error in function: " + e.function)
            return HttpResponse(e.message, status=e.status_code)

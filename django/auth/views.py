import environ
from django.shortcuts import redirect
from django.http import HttpResponse
from urllib.parse import urlencode
import environ

# Env setup
env = environ.Env()
environ.Env.read_env()


# Given a dictionary with the key values of the params formats them into a valid string
def format_query_params(params):
    params_string = "?"

    for index, (key, value) in enumerate(params.items()):
        # avoids adding the & char at the first param
        if index != 0:
            params_string += "&"
        params_string += key + "=" + value

    return params_string


# First step into the 42 auth workflow, redirects to the page were the user will enter their 42 credentials
def get_redirect_url():
    url = 'https://api.intra.42.fr/oauth/authorize'

    params = {
        "client_id": env('FT_API_UID'),
        "redirect_uri": env('FT_API_REDIRECT'),
        "response_type": "code",
        'scope': 'public',
    }

    url += format_query_params(params)

    print("url:", url)
    return url


# Entry point for 42 auth handling
def ft_auth(request):
    endpoint = get_redirect_url()
    return redirect(endpoint)

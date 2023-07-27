from django.shortcuts import render
# django-environ
import environ
env = environ.Env()
environ.Env.read_env()

import pyrebase
import os

# React frontEnd Build View
def react(request):
    return render(request, "index.html")

# def react(request):
#     context = { }
#     return render(request, "index.html", context)


# config = {
#     "apiKey": "KEY",
#     "authDomain": env('AUTH_DOMAIN'),
#     "projectId": "project_name-id",
#     "storageBucket": "project_name-id.appspot.com",
#     "messagingSenderId": "msg_sender_id",
#     "appId": "1:app_id",
#     "measurementId": "G-measurement_id",
#     "databaseURL": ""
# }

# firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()

# storage = firebase.storage()
# storage.child(PATH/DIRECTORY_ON_CLOUD).put(PATH_TO_LOCAL_IMAGE  )

from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.


def homePageView(request):
    """ Respond with a simple request"""
    url = "www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=2"

    payload={}
    headers = {
    'Cookie': 'kohanasession=5a05ae87b671e72a606e5c6b1fda500f; kohanasession_data=c2Vzc2lvbl9pZHxzOjMyOiI1YTA1YWU4N2I2NzFlNzJhNjA2ZTVjNmIxZmRhNTAwZiI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MjI6IlBvc3RtYW5SdW50aW1lLzcuMjYuMTAiO2lwX2FkZHJlc3N8czoxMjoiOTguMjI5LjczLjI4IjtsYXN0X2FjdGl2aXR5fGk6MTYxNjcxNjA3NDs%3D'
    }
    response1 = requests.request("GET", url, headers=headers, data=payload)


    return response1.text

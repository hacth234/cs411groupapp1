from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,CreateView, UpdateView
from .models import *
from .forms import *
import requests


# Create your views here.


# def searchPageView(request):


class CreateSearchRecipeView(CreateView):
    """ A view of Search form"""
    model = Recipe #whcih quote to create
    form_class = CreateSearchRecipeForm
    template_name = "displayapis/simple_recipe_search_api.html"

class ShowRecipePageView(DetailView):
    """ Shows one Recipe record"""
    model = Recipe
    template_name = "displayapis/display_recipe_json.html"
    context_object_name = "recipe"


class CreateSearchSymptomView(CreateView):
    """ A view of Search form"""
    model = Symptom #which quote to create
    form_class = CreateSearchSymptomForm
    template_name = "displayapis/simple_symptom_search_api.html"

class ShowSymptomPageView(DetailView):
    """ Shows one Recipe record"""
    model = Symptom
    template_name = "displayapis/display_fda_json.html"
    context_object_name = "symptom"


# class CreateSearchSymptomView(CreateView):
#     """ A view of Search form"""
#     model = Recipe #whcih quote to create
#     form_class = CreateSearchRecipeForm
#     template_name = "displayapis/simple_recipe_search_api.html"

def homePageView(request):
    """ Respond with a simple request"""

    url = "http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=2"

    payload={}
    headers = {
    'Cookie': 'kohanasession=5a05ae87b671e72a606e5c6b1fda500f; kohanasession_data=c2Vzc2lvbl9pZHxzOjMyOiI1YTA1YWU4N2I2NzFlNzJhNjA2ZTVjNmIxZmRhNTAwZiI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MjI6IlBvc3RtYW5SdW50aW1lLzcuMjYuMTAiO2lwX2FkZHJlc3N8czoxMjoiOTguMjI5LjczLjI4IjtsYXN0X2FjdGl2aXR5fGk6MTYxNjcxNjA3NDs%3D'
    }
    response1 = requests.request("GET", url, headers=headers, data=payload)


    url = "https://api.fda.gov/food/event.json?search=Diabetes&limit=10"

    payload={}
    headers = {}

    response2 = requests.request("GET", url, headers=headers, data=payload)
    response_html = """ 
    <html>
    <table>
        <h1> Displaying two different apis recipe puppy and fda.gov api </h1>
        <tr>
            <td> recipe puppy api json </td>
            <td> %s</td>
        </tr>
        <tr>
            <td> fda api json <td>
            <td> %s </td>
        </tr>
    </table>
    </html>
    """ % (response1.text, response2.text)

    return HttpResponse(response_html)

#unnecessary but here anyways
def recipeRequestView(request,pk):
    if request.method == 'POST':

        # create the form object from the request's POST data
        # form = CreateStatusMessageForm(request.POST or None)
        form = CreateSearchRecipeForm(request.POST or None)

        if form.is_valid():

            pass

    # redirect the user to the show_profile_page view
    url = reverse('jsonrecipeshow', kwargs={'pk': pk})
    return redirect(url)

def symptomRequestView(request):
    if request.method == 'POST':

        # create the form object from the request's POST data
        # form = CreateStatusMessageForm(request.POST or None)
        form = CreateSearchRecipeForm(request.POST or None)

        if form.is_valid():

            pass

    # redirect the user to the show_profile_page view
    url = reverse('jsonsymptomshow', kwargs={'pk': pk})
    return redirect(url)



from django.db import models
from django.http import HttpResponse
import requests
from django.urls import reverse

# Create your models here.

# class RecipeIngredients(models.Model):
#     ingredient = models.TextField(blank=True)
#     def __str__(self):
#         """ Return a string representation of this Ingredient."""
#         return f'{self.ingredient}'
# class RecipeDish(models.Model):
#     dish = models.TextField(blank=True)
#     def __str__(self):
#         """ Return a string representation of this dish."""
#         return f'{self.dish}'


class Recipe(models.Model):
    ingredient = models.TextField(blank=True)
    dish = models.TextField(blank=True)
    def __str__(self):
        """ Return a string representation of this dish."""
        return f'{self.dish} - {self.ingredient}'

    def get_absolute_url(self):
        """ gets an absolute url to redirect to """
        #gives back a reverse lookup for the quote which directs to the url quote thing
        #uses the name as label in the reverse function from the urls.py file
        return reverse('jsonrecipeshow', kwargs={'pk':self.pk})

    def get_json_objects(self):
        """ building the html to give """
        url = f"http://www.recipepuppy.com/api/?i={self.ingredient}&q={self.dish}&p=2"
        payload={}
        # headers = {
        #     'Cookie': 'kohanasession=5a05ae87b671e72a606e5c6b1fda500f; kohanasession_data=c2Vzc2lvbl9pZHxzOjMyOiI1YTA1YWU4N2I2NzFlNzJhNjA2ZTVjNmIxZmRhNTAwZiI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MjI6IlBvc3RtYW5SdW50aW1lLzcuMjYuMTAiO2lwX2FkZHJlc3N8czoxMjoiOTguMjI5LjczLjI4IjtsYXN0X2FjdGl2aXR5fGk6MTYxNjcxNjA3NDs%3D'
        #     }
        headers = {
        'Cookie': 'kohanasession=6ef039996c113872197775ac10e52255; kohanasession_data=c2Vzc2lvbl9pZHxzOjMyOiI2ZWYwMzk5OTZjMTEzODcyMTk3Nzc1YWMxMGU1MjI1NSI7dG90YWxfaGl0c3xpOjI7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MjI6IlBvc3RtYW5SdW50aW1lLzcuMjYuMTAiO2lwX2FkZHJlc3N8czoxMjoiOTguMjI5LjczLjI4IjtsYXN0X2FjdGl2aXR5fGk6MTYxNjczMTM5NDs%3D'
        }

        # headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        response_html = """
                %s
         """ % response.text

        return response_html

    # def get_json_objects(self):
    #     """ building the html to give """
    #     url = f"http://www.recipepuppy.com/api/?i={self.ingredient}&q={self.dish}&p=1"
    #     payload={}
    #     headers = {
    #         'Cookie': 'kohanasession=5a05ae87b671e72a606e5c6b1fda500f; kohanasession_data=c2Vzc2lvbl9pZHxzOjMyOiI1YTA1YWU4N2I2NzFlNzJhNjA2ZTVjNmIxZmRhNTAwZiI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MjI6IlBvc3RtYW5SdW50aW1lLzcuMjYuMTAiO2lwX2FkZHJlc3N8czoxMjoiOTguMjI5LjczLjI4IjtsYXN0X2FjdGl2aXR5fGk6MTYxNjcxNjA3NDs%3D'
    #         }
    #     # headers = {
    #     #     'Cookie': 'kohanasession=6ef039996c113872197775ac10e52255; kohanasession_data=c2Vzc2lvbl9pZHxzOjMyOiI2ZWYwMzk5OTZjMTEzODcyMTk3Nzc1YWMxMGU1MjI1NSI7dG90YWxfaGl0c3xpOjE7X2tmX2ZsYXNoX3xhOjA6e311c2VyX2FnZW50fHM6MjI6IlBvc3RtYW5SdW50aW1lLzcuMjYuMTAiO2lwX2FkZHJlc3N8czoxMjoiOTguMjI5LjczLjI4IjtsYXN0X2FjdGl2aXR5fGk6MTYxNjcyODg2Mzs%3D'
    #     # }
    #     response = requests.request("GET", url, headers=headers, data=payload)

    #     return response.text

class Symptom(models.Model):
    symptom = models.TextField(blank=True)
    def __str__(self):
        """ Return a string representation of this symptom."""
        return f'{self.symptom}'

    def get_absolute_url(self):
        """ gets an absolute url to redirect to """
        #gives back a reverse lookup for the quote which directs to the url quote thing
        #uses the name as label in the reverse function from the urls.py file
        return reverse('jsonsymptomshow', kwargs={'pk':self.pk})

    def get_json_objects(self):
        """ building the html to give """
        url = f"https://api.fda.gov/food/event.json?search={self.symptom}&limit=5"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response_html = """
            %s 
        """ % response.text

        return response_html



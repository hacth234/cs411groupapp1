
from django.urls import path
from django.urls import reverse
from .views import *


urlpatterns = [
    path('', homePageView, name='home'),
    path('test', homePageView, name='testapis'),
    path('searchrecipe', CreateSearchRecipeView.as_view(), name='searchrecipes'),
    path('searchrecipe/<int:pk>', ShowRecipePageView.as_view(), name='jsonrecipeshow'),
    path('searchsymptom', CreateSearchSymptomView.as_view(), name='searchsymptom'),
    path('searchsymptom/<int:pk>', ShowSymptomPageView.as_view(), name='jsonsymptomshow'),
]
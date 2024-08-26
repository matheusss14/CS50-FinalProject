from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guesser/<int:days>', views.guesser, name='guesser'),
    path('guesser/search/<str:player>', views.search, name="search"),
    path('guesser/getteam/<int:id>', views.get_team, name='get_team'),
    path('guesser/search/autocomplete/<str:player>', views.autofill, name='autofill'),
]
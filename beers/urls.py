from django.urls import path

from beers.views import first_view

urlpatterns = [
    path('', first_view, name='first-view'),
]
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first_view(request):

    vals = {
        'sample': 'Prueba de variable',
    }

    return render(request, 'beers.html', context=vals)

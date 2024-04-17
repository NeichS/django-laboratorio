from django.shortcuts import render
import pycountry

# Create your views here.

paises = list(pycountry.countries)
paises_dict = {pais.alpha_2: pais.name for pais in paises}


def index(request):
    return render(request, 'index.html', {'paises_dict': paises_dict})


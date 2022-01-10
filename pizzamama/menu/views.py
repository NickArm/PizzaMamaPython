from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

#Create views Here
#/menu
def index(request):
    '''pizzas=Pizza.objects.all()
    pizzas_names_and_price = [pizza.name + " : " + str(pizza.price) + "$" for pizza in pizzas]
    pizzas_names_and_price_str=", ".join(pizzas_names_and_price)
    return HttpResponse("Our Pizzas: "+ pizzas_names_and_price_str)'''
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas': pizzas})

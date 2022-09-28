from multiprocessing import context
from django.shortcuts import render
from mainapp.models import *

# Create your views here.
def main(request):
    return render(request, 'base.html')
def second(request):
    meals = Meals.objects.all()
    category = Category.objects.all()
    context1 = {'meals': meals, 'category': category}
    return render(request, 'index.html',
    context=context1)
    
    


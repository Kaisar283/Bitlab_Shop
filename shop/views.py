from django.shortcuts import render
from .models import Categories
# Create your views here.

def home(request):
    categories = Categories.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'index.html', context=context)
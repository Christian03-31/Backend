from django.shortcuts import render

def home(request):
    return render(request, 'presentacion/home.html')

# Create your views here.

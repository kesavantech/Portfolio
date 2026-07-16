from django.shortcuts import render
from Myapp.models import Portfolio

# Create your views here.
def HomeView(request):
    return render(request, "Home.html")

def IndexView(request):
    return render(request, "index.html")

def PortfolioView(request):
    name = request.models
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "powerball/home.html")

def drawing(request):
    return render(request, "powerball/drawing.html")
    
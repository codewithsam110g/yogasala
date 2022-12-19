from django.shortcuts import render

# Create your views here.
def competitions(request):
    return render(request, "competitions.html")
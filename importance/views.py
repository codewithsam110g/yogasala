from django.shortcuts import render

# Create your views here.
def importance(request):
    return render(request, "importance.html")
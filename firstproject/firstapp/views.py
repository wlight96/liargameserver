from django.shortcuts import render

def welcom(request):
    return render(request, "welcome.html")
from django.shortcuts import render

def myresume(request):
    return render(request,"index.html")
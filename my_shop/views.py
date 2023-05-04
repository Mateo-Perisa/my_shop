from django.shortcuts import render
from django import forms

# Create your views here.


def index(request):
    return render (request, 'index.html')

def prijava(request):
    return render(request, "prijava.html")

def o_nama(request):
    return render(request, "o_nama.html")

def novosti(request):
    return render(request, "novosti.html")

def kontakt(request):
    return render(request, "kontakt.html")

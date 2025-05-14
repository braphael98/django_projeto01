from django.shortcuts import render
from django.http import HttpResponse

# Aqui são criadas as views

def index(request):
    return HttpResponse('<h1> Projeto python ! <h1>')

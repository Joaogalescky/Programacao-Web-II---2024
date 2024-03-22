from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index da pagina de aluno")
# Create your views here.

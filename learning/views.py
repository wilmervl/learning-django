import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def home(request):
  usuario = { 
    "nombre_persona": "nombre", 
    "apellido": "Juan",
    "now": datetime.datetime.now(),
    "articles":["sapato","camisa","blusa","medias","polo"]
    
  }

  doc_externo = loader.get_template('index.html')

  document = doc_externo.render(usuario)

  return HttpResponse(document)

# with render
def home2(request):
  usuario = { 
    "nombre_persona": "nombre", 
    "apellido": "Juan",
    "now": datetime.datetime.now(),
    "articles":["sapato","camisa","blusa","medias","polo"]
    
  }



  return render(request, "base.html",usuario)

def curso(request):
  return render(request, "cursoC.html", {'age': 2021})
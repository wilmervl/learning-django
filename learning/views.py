import datetime
from django.http import HttpResponse
from django.template import Template, Context

def home(request):
  doc_externo = open("C:/Users/Wilmer/Dev/@Python/@Django/learning-django/learning/templates/index.html")
  plt = Template(doc_externo.read())
  doc_externo.close()

  usuario = { 
    "nombre_persona": "nombre", 
    "apellido": "Juan",
    "now": datetime.datetime.now()
  }

  ctx = Context(usuario)

  document = plt.render(ctx)

  return HttpResponse(document)
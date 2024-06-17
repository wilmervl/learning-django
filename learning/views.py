import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader

def home(request):
  # doc_externo = open("./learning/templates/index.html")
  # plt = Template(doc_externo.read())
  # doc_externo.close()

  usuario = { 
    "nombre_persona": "nombre", 
    "apellido": "Juan",
    "now": datetime.datetime.now(),
    "articles":["sapato","camisa","blusa","medias","polo"]
  }

  doc_externo = loader.get_template('index.html')
  ctx = Context(usuario)

  # document = plt.render(ctx)
  document = doc_externo.render(ctx)

  return HttpResponse(document)
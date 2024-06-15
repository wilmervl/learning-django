
from django.http import HttpResponse
from django.template import Template, Context

def home(request):
  doc_externo = open("C:\\Users\\Wilmer\\Dev\\@Python\\@Django\\learning\\learning\\templates\\index.html")
  plt = Template(doc_externo.read())
  doc_externo.close()

  ctx = Context()

  document = plt.render(ctx)

  return HttpResponse(document)
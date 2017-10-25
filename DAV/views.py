#from django.shortcuts import render_to_response
#TEMPLATE_DIRS = ("c:\\Users\\Samyon\\PycharmProjects\\untitled\\DAV\\" )
#def index (request):
#    return render_to_response('statya1.html')





from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

f = open('DAV/statyi/statya1.html', 'r', encoding='utf-8')
f1 = f.read()

def index(request):
    return HttpResponse(f1)
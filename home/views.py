from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Приветствую на моём сайте. </br> "
                        "<a href=\"/statyi/DAV/\">Децентрализованные электронные валюты - ДЭВ</a> </br> "
    #<a href="sad">fdgfdfhfg</a>   <br>   
                        "33"
                        ""
                        "")



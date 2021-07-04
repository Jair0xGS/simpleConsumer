from django.http import HttpResponse
from django.db import connection
from django.template import loader
from django.shortcuts import render

# Create your views here.
from django.views import View
#view to handle index
class IndexView(View):
    def get(self,request):
        template = loader.get_template('index.html')
        context ={

        }
        return HttpResponse(template.render(context, request))
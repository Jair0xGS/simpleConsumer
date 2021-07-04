from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Zona
from .forms import ClientForm

# Create your views here.
from django.views import View
class IndexView(View):
    def get(self,request):
        context = {
        }
        template = loader.get_template('user\\index.html')
        return HttpResponse(template.render(context, request))
class ClientView(View):
    def get(self,request):
        zonas =Zona.objects.all()
        form = ClientForm(request.POST)
        context = {
            'zonas':zonas,
            'form':form,
        }
        template = loader.get_template('user\\create.html')
        return HttpResponse(template.render(context, request))

    def post(self,request):
        zonas =Zona.objects.all()
        form = ClientForm(request.POST)
        context = {
            'zonas':zonas,
            'form':form,
        }
        template = loader.get_template('user\\create.html')
        if form.is_valid():
            form.save()
            context['success']='pass all validations, inserting new client'
            return HttpResponse(template.render(context, request))
        else:
            print(form.errors)
            print(type(form.errors))

            errors=form.errors.as_data()
            print(type(errors))
            context['errors']=dict(errors)
        return HttpResponse(template.render(context, request))
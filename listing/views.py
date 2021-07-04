from django.http import HttpResponse
from django.db import connection
from django.template import loader
from django.shortcuts import render
from .models import Zona
from .forms import ClientForm, FindClientForm

# Create your views here.
from django.views import View
#view to handle index
class IndexView(View):
    def get(self,request):
        form = FindClientForm()
        context = {
            "form":form
        }
        template = loader.get_template('user\\index.html')
        return HttpResponse(template.render(context, request))
    def post(self,request):
        form = FindClientForm(request.POST)
        template = loader.get_template('user\\index.html')
        context = {
            "form":form
        }
        if form.is_valid():
            cursor=connection.cursor()
            query= "EXEC _RegistrarCliente @nombre = '{nombre}', @tipo = {tipo},@id='',@zona='',@ruc='',@Direccion='',@credito='',@tipocli=''".format(nombre=form.cleaned_data.get("nombre"), tipo =5)
            cursor.execute(query)
            context["resultados"]=cursor.fetchall()
        else:
            print(form.errors)

        return HttpResponse(template.render(context, request))

#view to handle client
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
            template = loader.get_template('user\\index.html')
            context['success']='pass all validations, inserting new client'
            return HttpResponse(template.render(context, request))
        else:
            print(form.errors)
            print(type(form.errors))

            errors=form.errors.as_data()
            print(type(errors))
            context['errors']=dict(errors)
        return HttpResponse(template.render(context, request))
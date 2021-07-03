from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Zona
from .forms import ClientForm

# Create your views here.


def index(request):
    zonas =Zona.objects.all()
    form = ClientForm()
    template = loader.get_template('user\\index.html')
    context = {
        'zonas':zonas,
        'success':'mensaje de success',
    }
    if request.method =='POST':
        form  = ClientForm(request.POST)
        if form.is_valid():
            context['success']='pass all validations, inserting new client'
    context['form']=form
    return HttpResponse(template.render(context, request))
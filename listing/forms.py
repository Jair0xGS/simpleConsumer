from django import forms
from .models import Zona, Cliente
from .validations import validate_ruc,validate_cliente

# form to find client by name
class FindClientForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=100)
    nombre.widget.attrs.update({'class': 'form-control'})

# form to create new Client
zonas = Zona.objects.all()
class ClientForm(forms.ModelForm):
    cliente = forms.CharField(label="ID Cliente",validators=[validate_cliente])
    cliente.widget.attrs.update({'class': 'form-control'})

    nombre = forms.CharField(label="Nombre")
    nombre.widget.attrs.update({'class': 'form-control'})

    ruc = forms.IntegerField(label="RUC",validators=[validate_ruc])
    ruc.widget.attrs.update({'class': 'form-control'})

    zona = forms.ModelChoiceField(zonas)
    zona.widget.attrs.update({'class': 'form-control'})

    direccion= forms.CharField(label="Direccion")
    direccion.widget.attrs.update({'class': 'form-control'})

    credito = forms.BooleanField(label="Con Credito",required=False)
    credito.widget.attrs.update({'class': 'form-check-input'})

    tipoCliente= forms.ChoiceField(
        label='Tipo Cliente',
        choices=(
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
        ), 
        widget=forms.RadioSelect
    )
    tipoCliente.widget.attrs.update(
        {'class': 'form-check-input'})
    class Meta :
        model = Cliente
        fields = [
            'cliente',
            'nombre',
            'ruc',
            'zona',
            'direccion',
            'credito',
            'tipoCliente',

        ]
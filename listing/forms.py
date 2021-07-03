from django import forms
from .models import Zona,Cliente
from .validations import validate_ruc


class ClientForm(forms.ModelForm):
    #zonas = Zona.objects.all()
    cliente= forms.CharField(label="ID Cliente")
    cliente.widget.attrs.update({'class': 'form-control'})
    nombre= forms.CharField(label="Nombre")
    nombre.widget.attrs.update({'class': 'form-control'})
    zonaid = forms.Mode
   #zonaid= forms.ChoiceField(
   #    label="Zona",
   #    choices=[
   #        (
   #            zn.zona,
   #            zn.descripcion
   #            + ' - '
   #            +zn .ciudad
   #        ) for zn in zonas
   #    ]

   #)
   #zonaid.widget.attrs.update({'class': 'form-control'})
    ruc = forms.IntegerField(label="RUC",validators=[validate_ruc])
    ruc.widget.attrs.update({'class': 'form-control'})
    direccion= forms.CharField(label="Direccion")
    direccion.widget.attrs.update({'class': 'form-control'})
    credito = forms.BooleanField(label="Con Credito")
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
            'zona',
            'ruc',
            'direccion',
            'credito',
            'tipoCliente',

        ]

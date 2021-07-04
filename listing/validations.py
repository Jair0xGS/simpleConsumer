from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_ruc(value):
    if value <=10000000000 or value >= 99999999999 :
        raise ValidationError(
            _('%(value)s no es un RUC valido,debe tener 11 caracteres'),
            params={'value': value},
        )
def validate_cliente(value):
    if len(value)!= 4:
        raise ValidationError(
            _('Cliente debe tener 4 caracteres'),
            params={'value': value},
        )
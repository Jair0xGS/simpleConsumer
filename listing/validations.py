from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_ruc(value):
    if value <=10000000000 or value >= 99999999999 :
        raise ValidationError(
            _('%(value)s no es un RUC valido'),
            params={'value': value},
        )
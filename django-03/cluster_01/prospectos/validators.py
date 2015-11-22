import re
from django.core.exceptions import ValidationError

def validate_dni(value):
    if not bool(re.match(r'^[0-9]{8}$', value)):
        raise ValidationError('%s is not a valid DNI' % value)

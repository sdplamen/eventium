import re
from django.core.exceptions import ValidationError


def company_name(value):
    if not re.match(r'^[A-Za-z0-9\s\-]+$', value):
        raise ValidationError('The company name is invalid!')

def secret_key(value):
    if not value.isdigit() or len(value) != 4 or len(set(value)) != 4:
        raise ValidationError("Your secret key must have 4 unique digits!")
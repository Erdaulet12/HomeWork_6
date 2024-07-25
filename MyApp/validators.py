from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_positive_or_zero(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a positive number, including zero'),
            params={'value': value},
        )

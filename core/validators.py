# Django: Validator
from django.core.validators import RegexValidator

username_validator = RegexValidator(r"[a-zA-Z-_\d+\.]+")

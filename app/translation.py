import re 
from django.core.exceptions import ValidationError

KYRGYZ_PUSSIAN_REGEX = r"[А-Яа-яЁёҢңӨөҮү\- ]+"

def validate_kyrgyz_russian_letter(value):
    if not re.fullmatch(KYRGYZ_PUSSIAN_REGEX, value):
        raise ValidationError(
            "Поле может содержать только кыргызские и русские буквы"
        )
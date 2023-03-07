from django.db import models
from django.contrib.auth.models import User
ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIPClient"),
    (CLIENT, "CLIENT")
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER")
)


COUNTRY = (
    (KYRGYZSTAN, 'KYRGYZSTAN'),
    (RUSSIA, 'RUSSIA'),
    (UZBEKISTAN, 'UZBEKISTAN')
)

EYE = (
    (BROWN, 'BROWN'),
    (YELLOW, 'YELLOW'),
    (GREEN, 'GREEN'),
    (BLACK, 'BLACK')
)


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип Пользователя')
    phone_number = models.CharField('номер телефона', max_length=20)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')
    country = forms.ChoiceField(choices=COUNTRY, max_length=20)
    telegram = forms.CharField('your telegram nick', max_length=20)
    born_day = forms.CharField(required=True)
    eye_color = forms.ChoiceField(choices=EYE, required=True)
    foot_size = forms.CharField(required=True)
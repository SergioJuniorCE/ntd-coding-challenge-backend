from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

import re

UserModel = get_user_model()


def user_validation(data):
    username = data['username'].strip()
    password = data['password'].strip()
    ##
    if not username or UserModel.objects.filter(username=username).exists():
        raise ValidationError('choose another email')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    return data


def validate_username(data):
    # Check if email is valid with regex
    emailRegex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    username = data['username'].strip()
    if not re.match(emailRegex, username):
        raise ValidationError('choose another username')
    return True


def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True

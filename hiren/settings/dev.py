from .base import *
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
try:
    with open('config.local.json') as f:
        JSON_DATA = json.load(f)
except FileNotFoundError:
    with open('config.json') as f:
        JSON_DATA = json.load(f)

SECRET_KEY = os.environ.get('SECRET_KEY', JSON_DATA['secret_key'])


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass

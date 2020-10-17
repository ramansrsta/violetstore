from .base import *
import os
from pathlib import Path
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': BASE_DIR / '',
    }
}

MEDIA_URL = '//'
MEDIA_ROOT = os.path.join(BASE_DIR,'')
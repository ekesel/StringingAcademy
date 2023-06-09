"""
Django settings for stringing project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['stringing.co.in','www.stringing.co.in']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'constance',
    'constance.backends.database',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stringing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stringing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'assets')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Base url to serve media files  
MEDIA_URL = '/media/'  
    
# Path where media is stored  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMINS = (('Stringing', 'stringingmusic2023@gmail.com'),)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_HOST_USER = env('EMAIL')
EMAIL_HOST_PASSWORD = env('PASSWORD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'Stringing <stringingmusic2023@gmail.com>'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

CONSTANCE_ADDITIONAL_FIELDS = {
    'file_field': ['django.forms.FileField', {}]
}

CONSTANCE_CONFIG = {
    'PRIVACY_POLICY': ('', 'Privacy Policy', 'file_field'),
    'CANCELLATION_POLICY': ('', 'Cancellation/Refund Policy', 'file_field'),
    'TERMS_POLICY': ('', 'Terms and Conditions', 'file_field'),
    'ABOUT_US_HEADER': ('', 'The heading of the About us page'),
    'ABOUT_US_CONTENT': ('', 'About Us Content'),
    'ABOUT_US_SUB_HEADER': ('', 'About Us Subheading'),
    'INSTAGRAM_LINK': ('', 'Instagram Follow Link'),
    'FACEBOOK_LINK': ('', 'Facebook Follow Link'),
    'CONTACT_PHONE': ('', 'Phone in Contact Page'),
    'CONTACT_EMAIL': ('', 'Email in Contact Page'),
    'CONTACT_ADDRESS': ('', 'Address in Contact Page'),
    'BANNER_FIRST_LINE': ('21 DAYS GUITAR', 'The first line of banner'),
    'BANNER_SECOND_LINE': ('WORKSHOP','Second line of banner'),
    'BANNER_THIRD_LINE': ('IN AZAMGARH', 'Third line of banner'),
    'BANNER_FOURTH_LINE': ('FRIDAY, 7 APRIL 2023', 'Fourth small line of banner'),
    'BANNER_FIFTH_LINE': ('Inside Tiny Tots School, Raidopur', 'Fifth small line of banner'),
    'BANNER_SIXTH_LINE': ('Register Below!', 'Last line of banner')
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Policies': ('PRIVACY_POLICY', 'CANCELLATION_POLICY', 'TERMS_POLICY'),
    'AboutUsPage': ('ABOUT_US_HEADER','ABOUT_US_CONTENT','ABOUT_US_SUB_HEADER'),   
    'FollowLinks' : ('INSTAGRAM_LINK', 'FACEBOOK_LINK'),
    'ContactPage': ('CONTACT_PHONE', 'CONTACT_EMAIL', 'CONTACT_ADDRESS'),
    'HomePage': ('BANNER_FIRST_LINE','BANNER_SECOND_LINE','BANNER_THIRD_LINE','BANNER_FOURTH_LINE','BANNER_FIFTH_LINE','BANNER_SIXTH_LINE')
}

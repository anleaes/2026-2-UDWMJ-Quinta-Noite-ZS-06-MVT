# Imports 
# os = manipulacao de funcoes do sistema operacional
# sys = funcoes para manipular partes do ambiente de tempo de execucao
# pathlib = 
# decouple = esconder os dados de conexao da oracle
import os
import sys
from pathlib import Path
from decouple import config

# Caminho dos diretorios de acesso do django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Registra o caminho dos apps
APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, APPS_DIR)

# Chave escondida no env
SECRET_KEY = config('SECRET_KEY')

# Arquivo tambem oculto no env
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'champions.apps.ChampionsConfig',
    'persons.apps.PersonsConfig',
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

ROOT_URLCONF = 'campeonatoapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'campeonatoapp.wsgi.application'


# Database
tns_admin = Path(os.getenv("TNS_ADMIN", "Wallet_campeonatoappdb"))

if not tns_admin.is_absolute():
    tns_admin = (BASE_DIR / tns_admin).resolve()

os.environ["TNS_ADMIN"] = str(tns_admin)

DATABASES= {     
    'default': {         
        'ENGINE': 'django.db.backends.oracle',         
        'NAME': config('TNS_NAME'),         
        'USER': config('DB_USER'),         
        'PASSWORD': config('DB_PASSWORD'),         
        'OPTIONS': {             
            'config_dir': config('TNS_ADMIN'),             
            'wallet_location': config('TNS_ADMIN'),             
            'wallet_password': config('WALLET_PASSWORD'),
        },     
    } 
}


# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

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


# Linguagem e timezone do app

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Arquivos estaticos (CSS, JavaScript, Imagens)

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

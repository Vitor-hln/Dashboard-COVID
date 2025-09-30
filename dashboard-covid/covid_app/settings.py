import os
from dotenv import load_dotenv
from pathlib import Path





BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega as variáveis de ambiente do arquivo .env
SECRET_KEY = os.environ.get('SECRET_KEY')

# Segurança - Não deixar DEBUG ativo em produção
DEBUG = True
                       
ALLOWED_HOSTS = ["*", "127.0.0.1", "localhost"]



#CSRF_TRUSTED_ORIGINS = [
#    origin.strip() for origin in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')
#    if origin.strip()

 
 # Database BASE DO DJANGO
#DATABASES = {
# 'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
# }
#}


DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('POSTGRES_DB', 'covid_dashboard'),
        'USER': os.getenv('POSTGRES_USER', 'user_db'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'senha_db'),
        'HOST': os.getenv('POSTGRES_HOST', 'postgres_demonstrativo'),
        'PORT': os.getenv('POSTGRES_PORT', '5432')
    }
}
        

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
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

ROOT_URLCONF = 'covid_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'covid_app.wsgi.application'

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

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Diretório onde o collectstatic vai coletar TODOS os arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diretórios adicionais onde o Django procura por arquivos estáticos
# (além dos diretórios static/ dentro de cada app)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Se estiver usando WhiteNoise para servir arquivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#  USAR QUANDO NECESSARIO 

#AUTH_USER_MODEL = 'auth.User'
#
#LOGIN_REDIRECT_URL = '/'
#LOGOUT_REDIRECT_URL = '/login/'
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Does not matter is this is here it is not used

# SECURITY WARNING: don't run with debug turned on in production!

BRANCH = 'main'
DEBUG = True

if (BRANCH == 'dev'):
    DEBUG = True
    SECRET_KEY = 'django-insecure--4miyw_-w8w6o+eb$k2h@d8e@*cm_4=4g4%amy2pvpm%p5mtbm'
    #
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db',
            'USER': 'db',
            'PASSWORD': 'AVNS_GX5VbMbiWBMTiDTjlIA',
            'HOST': 'app-f0094673-bf2f-464d-bb75-b68efd471570-do-user-3900047-0.b.db.ondigitalocean.com',
            'PORT': '25060',
        }
    }


elif (BRANCH == 'main'):
    DEBUG = True
    SECRET_KEY = 'Override_with_env_viriable_by_the_provider'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db',
            'USER': 'db',
            'PASSWORD': 'AVNS_GX5VbMbiWBMTiDTjlIA',
            'HOST': 'app-f0094673-bf2f-464d-bb75-b68efd471570-do-user-3900047-0.b.db.ondigitalocean.com',
            'PORT': '25060',
        }
    }

ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'info_api.apps.InfoApiConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Needed to allow cross site data transfer via api
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "https://elegant-kelpie-09cfe4.netlify.app",
    "https://www.johncruz.dev",
    "https://johncruz.dev",
]

AUTH_USER_MODEL = 'info_api.Account'

ROOT_URLCONF = 'resume_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'resume_project.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

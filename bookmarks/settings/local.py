from .base import*

DEBUG = True,
ALLOWED_HOSTS = []

SECRET_KEY = '%#+nou&*v((=kdlk1#k^g8(cdpnpdr&0bqg+9nqxu2+b)0$gyf'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gu%-gkyxf(g#2-5^%vk8_qgmg6m=uqk-05x4@=6jjm@6tu)u2l'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}

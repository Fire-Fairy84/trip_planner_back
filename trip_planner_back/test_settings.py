from .settings import *  # Importa la configuración base

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Usa PostgreSQL como motor
        'NAME': 'test_travel_planner',  # Nombre de la base de datos de pruebas
        'USER': 'postgres',  # Usuario de la base de datos
        'PASSWORD': '1321',  # Contraseña de la base de datos
        'HOST': 'localhost',  # Dirección del host
        'PORT': '5432',  # Puerto por defecto de PostgreSQL
    }
}

# Desactiva la caché para evitar conflictos durante las pruebas
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

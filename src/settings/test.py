from .base import *

ALLOWED_HOSTS = ['*']

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Media storage
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

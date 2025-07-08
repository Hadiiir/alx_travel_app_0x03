# Celery Configuration (with environment variables)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@localhost:5672//')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = os.getenv('TIMEZONE', 'UTC')

# Security enhancements
CELERY_TASK_IGNORE_RESULT = False  # Only store results when needed
CELERY_TASK_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

# Email Configuration (with environment variables)
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
SERVER_EMAIL = os.getenv('SERVER_EMAIL', EMAIL_HOST_USER)

# Email timeout settings
EMAIL_TIMEOUT = 30  # seconds

from dotenv import load_dotenv
load_dotenv()
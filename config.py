import os

BASE_DIR = os.path.relpath(os.path.dirname(__file__))

DEBUG = True

CSRF_ENABLED = True
CSRF_SESSION_KEY = '15018ed6-927a-46ea-8953-7db263079f56'
SECRET_KEY = 'b7075b09-ee60-4abb-9bea-2d36747bf3ff'

PERMANENT_SESSION_LIFETIME = 3600
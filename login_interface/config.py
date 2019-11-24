from os import environ

ENV = 'production'

SECRET_KEY = '4ccfdc4e1da352c1475e44d838c13df3'

# TODO: Database configuration
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
DATABASE = 'flask_login'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# TODO: Email configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

MAIL_USERNAME = environ.get('EMAIL_USER')
MAIL_PASSWORD = environ.get('EMAIL_PASSWORD')

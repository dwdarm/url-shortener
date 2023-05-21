import environ
import os

from pathlib import Path

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, 'thisissecret'),
    BASE_DOMAIN=(str, 'http://localhost:5000'),
    MONGODB_URI=(str, 'mongodb://localhost:27017/'),
)

environ.Env.read_env()

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

BASE_DOMAIN = env('BASE_DOMAIN')

MONGODB_URI = env('MONGODB_URI')

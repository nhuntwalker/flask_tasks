"""Configuration for the application."""
import os
basedir = os.path.dirname(__file__)


class Config(object):
    """Configuration settings for the flask-tasks app."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', '')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')


class ProductionConfig(Config):
    """Specific configuration settings for production."""

    DEBUG = False


class DevelopmentConfig(Config):
    """Specific configuration settings for development."""

    DEBUG = True
    DEVELOPMENT = True

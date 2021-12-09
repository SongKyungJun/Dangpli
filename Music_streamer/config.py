from django.apps import AppConfig


class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
    label = 'apps'

class MyConfig(AppConfig):
    name = 'apps.home'
    label = 'apps_home'

class AuthConfig(AppConfig):
    name = 'apps.auth'
    label = 'apps_auth'

from django.apps import AppConfig


class OceandbsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oceandbs'

    def ready(self):
      from . import tasks
      tasks.start()

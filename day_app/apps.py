import os
from django.apps import AppConfig


class DayAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'day_app'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            return True
        else:
            pass

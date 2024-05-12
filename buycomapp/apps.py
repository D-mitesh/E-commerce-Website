from django.apps import AppConfig


class BuycomappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buycomapp'

    def ready(self):
        import buycomapp.signals
from django.apps import AppConfig


class MinimartConfig(AppConfig):
    name = 'MiniMart'

    def ready(self):
        import MiniMart.signals

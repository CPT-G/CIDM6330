from django.apps import AppConfig


class EMPlanningApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'em_planning_api'

    def ready(self):
        import em_planning_api.signals

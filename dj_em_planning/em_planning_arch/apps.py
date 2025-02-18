from django.apps import AppConfig


class EMPlanningArchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'em_planning_arch'

    def ready(self):
        import em_planning_api.signals

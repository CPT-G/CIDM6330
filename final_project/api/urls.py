from django.urls import path, include
# from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r"bookmarks", views.BookmarkViewSet)
# router.register(r"snippets", views.SnippetViewSet)
# router.register(r"users", views.UserViewSet)
# router.register(r"learningpath", views.LearningPathViewSet)
# router.register(r"users", views.UserViewSet)

app_name = "api"

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem)
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("", include(router.urls)),
]

# add the router's URLs to the urlpatterns
# urlpatterns += router.urls

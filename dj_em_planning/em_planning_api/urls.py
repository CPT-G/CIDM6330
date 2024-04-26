from django.urls import path, include
# from rest_framework import routers

from em_planning_api import views as api_views

# router = routers.DefaultRouter()
# router.register(r"bookmarks", views.BookmarkViewSet)
# router.register(r"snippets", views.SnippetViewSet)
# router.register(r"users", views.UserViewSet)
# router.register(r"learningpath", views.LearningPathViewSet)
# router.register(r"users", views.UserViewSet)

# app_name = "em_planning_api"

urlpatterns = [
    # path('', api_views.CustomerView.as_view(), name="customer"),
    path('customers/', api_views.CustomerView.as_view(), name="customer"),
    path('customers/<int:pk>/', api_views.CustomerDetailView.as_view(),
         name="customer-detail")
    # path('', views.getData),
    # path('add/', views.addItem)
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("", include(router.urls)),
]

# add the router's URLs to the urlpatterns
# urlpatterns += router.urls

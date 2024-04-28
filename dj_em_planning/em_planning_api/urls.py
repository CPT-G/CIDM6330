from django.urls import path, include
# from rest_framework import routers

from em_planning_api import views as api_views
from rest_framework.authtoken import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# router = routers.DefaultRouter()
# router.register(r"bookmarks", views.BookmarkViewSet)
# router.register(r"snippets", views.SnippetViewSet)
# router.register(r"users", views.UserViewSet)
# router.register(r"learningpath", views.LearningPathViewSet)
# router.register(r"users", views.UserViewSet)

# localhost:8000/em_planning_api/ (customers/auth/token/etc)

# app_name = "em_planning_api"

urlpatterns = [
    path('customers/', api_views.CustomerView.as_view(), name="customer"),
    path('customers/<int:pk>/', api_views.CustomerDetailView.as_view(),
         name="customer-detail"),
    path('auth/', include('rest_authtoken.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
# path('', views.getData),
# path('add/', views.addItem)
# path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
# path("", include(router.urls)),

# add the router's URLs to the urlpatterns
# urlpatterns += router.urls

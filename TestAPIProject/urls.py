from django.urls import path, include
from API.urls import urlpatterns as user_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include(user_urls)),
]

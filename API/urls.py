from django.urls import path
from .views import UsersList, UserDetail

urlpatterns = [
    path('api/users/', UsersList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

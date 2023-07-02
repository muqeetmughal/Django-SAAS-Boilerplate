from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]

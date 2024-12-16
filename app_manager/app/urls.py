from django.urls import path
from .views import add_app, get_app, delete_app

urlpatterns = [
    path('add-app/', add_app, name='add-app'),
    path('get-app/<int:id>/', get_app, name='get-app'),
    path('delete-app/<int:id>/', delete_app, name='delete-app'),
]

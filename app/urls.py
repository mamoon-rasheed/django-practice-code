from django.urls import path
from .views import hello, nameidentifier, ageidentifier

urlpatterns = [
    path('hello', hello),
    path('nameidentifier/<name>', nameidentifier),
    path('ageidentifier/<int:age>', ageidentifier),
]

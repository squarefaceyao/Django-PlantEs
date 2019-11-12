from django.urls import path
from Book.views import test

urlpatterns = [
    path('test/', test)
]


from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('criptografia',views.cifrar),
    path('criptografia/codificar',views.codificar),
    path('',views.cifrar),
]
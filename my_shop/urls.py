from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("prijava", views.prijava, name="prijava"),
    path("o_nama", views.o_nama, name="o_nama"),
    path("novosti", views.novosti, name="novosti"),



] 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('form_add/', views.form_add),
    path('form_add/agregar', views.agregar),
    path('form_edit/<int:id>', views.form_edit),
    path('form_edit/actualizar/<int:id>', views.actualizar),
    path('borrar/<int:id>', views.borrar)
]

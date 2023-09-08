from django.urls import path
from .views import home, save, editar, update, delete, getAll, get, deleteConfirm

urlpatterns = [
    path('', home, name="home-ecopontos"),
    path('get/', getAll, name="get-all-ecopontos"),
    path('get/<int:id>', get, name="get-ecoponto"),
    path('save/', save, name="save-ecoponto"),
    path('update/<int:id>', update, name="update-ecoponto"),
    path('editar/<int:id>', editar, name="editar-ecoponto"),
    path('delete/<int:id>', delete, name="delete-ecoponto"),
    path('delete-confirm/<int:id>', deleteConfirm, name="delete-confirm-ecoponto"),
]

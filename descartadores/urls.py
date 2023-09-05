from django.urls import path
from .views import home, getAll, get, save, update, editar, delete, \
    deleteConfirm

urlpatterns = [
    path('', home, name="home-descartadores"),
    path('get/', getAll, name="get-all-descartadores"),
    path('buscar/<int:documento>', get, name="buscar-descartadores"),
    path('save/', save, name="save-descartadores"),
    path('update/<int:documento>', update, name="update-descartadores"),
    path('editar/<int:documento>', editar, name="editar-descartadores"),
    path('delete/<int:documento>', delete, name="delete-descartadores"),
    path('delete-confirm/<int:documento>', deleteConfirm, name="delete-confirm-descartadores"),
]

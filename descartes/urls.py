from django.urls import path
from .views import home, save, editar, update, delete, getAll, get, deleteConfirm

urlpatterns = [
    path('', home, name="home-descartes"),
    path('get/', getAll, name="get-all-descartes"),
    path('get/<int:id>', get, name="get-descartes"),
    path('save/', save, name="save-descartes"),
    path('update/<int:id>', update, name="update-descartes"),
    path('editar/<int:id>', editar, name="editar-descartes"),
    path('delete/<int:id>', delete, name="delete-descartes"),
    path('delete-confirm/<int:id>', deleteConfirm, name="delete-confirm-descartes"),
]

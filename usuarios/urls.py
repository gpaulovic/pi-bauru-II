from django.urls import path
from .views import home, save, editar, update, delete, getAll, get, deleteConfirm

urlpatterns = [
    path('', home, name="home-usuarios"),
    path('get/', getAll, name="get-all-usuarios"),
    path('get/<int:id>', get, name="get-usuarios"),
    path('save/', save, name="save-usuarios"),
    path('editar/<int:id>', editar, name="editar-usuarios"),
    path('update/<int:id>', update, name="update-usuarios"),
    path('delete/<int:id>', delete, name="delete-usuarios"),
    path('delete-confirm/<int:id>', deleteConfirm, name="delete-confirm-usuarios"),
]

from django.urls import path
from .views import UsuarioListCreate, UsuarioRetrieveUpdateDestroy, usuario_create_view

urlpatterns = [
    path("usuarios/", UsuarioListCreate.as_view(), name="usuario-list-create"),
    path(
        "usuarios/<int:pk>/", 
        UsuarioRetrieveUpdateDestroy.as_view(), 
        name="usuario-retrieve-update-destroy"
        ),
    path("usuarios/new/", usuario_create_view, name="usuario-create"),
]
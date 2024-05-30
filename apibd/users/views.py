from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
from .forms import UsuarioForm


class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def usuario_create_view(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario-list-create")
    else:
        form = UsuarioForm()
    
    return render(request, "usuario_form.html", {"form": form})

def usuario_delete_view(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == "POST":
        usuario.delete()
        return redirect("usuario-list-create")
    
    return render(request, "usuario_confirm_delete.html", {"usuario": usuario})

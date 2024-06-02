from django.shortcuts import render
from .models import Produto

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'core/index.html')
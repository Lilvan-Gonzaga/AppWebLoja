

from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Produto, Categoria
from .forms import ProdutoForm

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'core/lista_produto.html', {'produtos': produtos})


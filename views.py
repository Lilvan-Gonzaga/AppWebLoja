from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Produto
from .forms import ProdutoForm

# View para listar produtos disponíveis
def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'core/home.html', {'produtos': produtos})

def lista_produtos_admin(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'core/home_adm.html', {'produtos': produtos})

# View para adicionar produtos
def adc_produtos(request):
    if request.method == 'POST':  # Se o método for POST
        form = ProdutoForm(request.POST, request.FILES)  # Pega as informações do formulário
        if form.is_valid():  # Se o formulário for válido
            form.save()  # Salva o produto
            messages.success(request, 'O produto foi criado com sucesso')  # Mensagem de sucesso
            return HttpResponseRedirect(reverse('home'))  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm()  # Senão, carrega o formulário vazio
    return render(request, 'core/adc_produto.html', {'form': form})  # Renderiza o template

# View para atualizar produtos
def update_produtos(request, id):
    produto = get_object_or_404(Produto, id=id)  # Pega o produto pelo ID
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)  # Pega as informações do formulário
    if form.is_valid():  # Se o formulário for válido
        form.save()  # Salva as alterações
        messages.warning(request, 'O produto foi atualizado com sucesso')  # Mensagem de sucesso
        return HttpResponseRedirect(reverse('home'))  # Redireciona para a lista de produtos
    return render(request, 'core/update_produto.html', {'form': form})  # Renderiza o template

# View para deletar produtos
def dell_produtos(request, id): 
    produto = get_object_or_404(Produto, id=id)  # Pega o produto pelo ID
    if request.method == 'POST':  # Se o método for POST
        produto.delete()  # Deleta o produto
        messages.error(request, 'O produto foi deletado com sucesso')  # Mensagem de sucesso
        return HttpResponseRedirect(reverse('home'))  # Redireciona para a lista de produtos
    return render(request, 'core/dell_produto.html')  # Renderiza o template
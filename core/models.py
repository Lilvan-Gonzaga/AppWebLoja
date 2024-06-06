from django.db import models


# Create your models here.
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.nome
    

    class Meta:  # adicionar isso
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']
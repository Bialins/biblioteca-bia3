
import uuid
from django.db import models


class Autor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name='livros',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    nome_leitor = models.CharField(max_length=150)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(blank=True, null=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.livro.titulo} - {self.nome_leitor}"

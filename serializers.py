
from rest_framework import serializers


class AutorInputSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=150)
    nacionalidade = serializers.CharField(
        max_length=100,
        required=False,
        allow_null=True,
        allow_blank=True
    )


class CategoriaInputSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    descricao = serializers.CharField(
        max_length=255,
        required=False,
        allow_null=True,
        allow_blank=True
    )


class LivroInputSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=200)
    isbn = serializers.CharField(max_length=20)
    autor_id = serializers.UUIDField()
    categoria_id = serializers.UUIDField(required=False, allow_null=True)


class EmprestimoInputSerializer(serializers.Serializer):
    livro_id = serializers.UUIDField()
    nome_leitor = serializers.CharField(max_length=150)

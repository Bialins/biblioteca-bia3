
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from dataclasses import asdict
from drf_spectacular.utils import extend_schema

from .services import (
    AutorService,
    CategoriaService,
    LivroService,
    EmprestimoService,
)
from .serializers import (
    AutorInputSerializer,
    CategoriaInputSerializer,
    LivroInputSerializer,
    EmprestimoInputSerializer,
)


class AutorListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    
    def get(self, request):
        service = AutorService()
        autores = service.listar()
        return Response([asdict(a) for a in autores], status=status.HTTP_200_OK)

    @extend_schema(request=CategoriaInputSerializer)
    def post(self, request):
        serializer = AutorInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AutorService()
        autor = service.criar(serializer.validated_data)
        return Response(asdict(autor), status=status.HTTP_201_CREATED)


class AutorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, autor_id):
        service = AutorService()
        autor = service.buscar_por_id(autor_id)
        return Response(asdict(autor), status=status.HTTP_200_OK)

    def put(self, request, autor_id):
        serializer = AutorInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AutorService()
        autor = service.atualizar(autor_id, serializer.validated_data)
        return Response(asdict(autor), status=status.HTTP_200_OK)

    def delete(self, request, autor_id):
        service = AutorService()
        service.remover(autor_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriaListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = CategoriaService()
        categorias = service.listar()
        return Response([asdict(c) for c in categorias], status=status.HTTP_200_OK)
    
    @extend_schema(request=CategoriaInputSerializer)
    def post(self, request):
        serializer = CategoriaInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CategoriaService()
        categoria = service.criar(serializer.validated_data)
        return Response(asdict(categoria), status=status.HTTP_201_CREATED)


class CategoriaDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, categoria_id):
        service = CategoriaService()
        categoria = service.buscar_por_id(categoria_id)
        return Response(asdict(categoria), status=status.HTTP_200_OK)

    @extend_schema(request=CategoriaInputSerializer)
    def put(self, request, categoria_id):
        serializer = CategoriaInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CategoriaService()
        categoria = service.atualizar(categoria_id, serializer.validated_data)
        return Response(asdict(categoria), status=status.HTTP_200_OK)

    def delete(self, request, categoria_id):
        service = CategoriaService()
        service.remover(categoria_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LivroListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = LivroService()
        livros = service.listar()
        return Response([asdict(l) for l in livros], status=status.HTTP_200_OK)

    @extend_schema(request=LivroInputSerializer)
    def post(self, request):
        serializer = LivroInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = LivroService()
        livro = service.criar(serializer.validated_data)
        return Response(asdict(livro), status=status.HTTP_201_CREATED)


class LivroDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, livro_id):
        service = LivroService()
        livro = service.buscar_por_id(livro_id)
        return Response(asdict(livro), status=status.HTTP_200_OK)

    def put(self, request, livro_id):
        serializer = LivroInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = LivroService()
        livro = service.atualizar(livro_id, serializer.validated_data)
        return Response(asdict(livro), status=status.HTTP_200_OK)

    def delete(self, request, livro_id):
        service = LivroService()
        service.remover(livro_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmprestimoListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = EmprestimoService()
        emprestimos = service.listar()
        return Response([asdict(e) for e in emprestimos], status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmprestimoInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = EmprestimoService()
        emprestimo = service.criar(serializer.validated_data)
        return Response(asdict(emprestimo), status=status.HTTP_201_CREATED)


class EmprestimoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, emprestimo_id):
        service = EmprestimoService()
        emprestimo = service.buscar_por_id(emprestimo_id)
        return Response(asdict(emprestimo), status=status.HTTP_200_OK)


class EmprestimoDevolucaoView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, emprestimo_id):
        service = EmprestimoService()
        emprestimo = service.devolver(emprestimo_id)
        return Response(asdict(emprestimo), status=status.HTTP_200_OK)

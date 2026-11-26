
from .models import Autor, Categoria, Livro, Emprestimo
from .dtos import AutorDTO, CategoriaDTO, LivroDTO, EmprestimoDTO


class AutorMapper:

    @staticmethod
    def to_dto(autor: Autor) -> AutorDTO:
        return AutorDTO(
            id=autor.id,
            nome=autor.nome,
            nacionalidade=autor.nacionalidade,
        )

    @staticmethod
    def to_entity(dados: dict, instancia: Autor = None) -> Autor:
        instancia = instancia or Autor()
        instancia.nome = dados.get('nome')
        instancia.nacionalidade = dados.get('nacionalidade')
        return instancia


class CategoriaMapper:

    @staticmethod
    def to_dto(categoria: Categoria) -> CategoriaDTO:
        return CategoriaDTO(
            id=categoria.id,
            nome=categoria.nome,
            descricao=categoria.descricao,
        )

    @staticmethod
    def to_entity(dados: dict, instancia: Categoria = None) -> Categoria:
        instancia = instancia or Categoria()
        instancia.nome = dados.get('nome')
        instancia.descricao = dados.get('descricao')
        return instancia


class LivroMapper:

    @staticmethod
    def to_dto(livro: Livro) -> LivroDTO:
        return LivroDTO(
            id=livro.id,
            titulo=livro.titulo,
            isbn=livro.isbn,
            autor_id=livro.autor_id,
            autor_nome=livro.autor.nome if livro.autor_id else None,
            categoria_id=livro.categoria_id,
            categoria_nome=livro.categoria.nome if livro.categoria_id else None,
        )

    @staticmethod
    def to_entity(dados: dict, instancia: Livro = None) -> Livro:
        instancia = instancia or Livro()
        instancia.titulo = dados.get('titulo')
        instancia.isbn = dados.get('isbn')
        instancia.autor_id = dados.get('autor_id') or dados.get('autor')
        instancia.categoria_id = dados.get('categoria_id') or dados.get('categoria')
        return instancia


class EmprestimoMapper:

    @staticmethod
    def to_dto(emprestimo: Emprestimo) -> EmprestimoDTO:
        return EmprestimoDTO(
            id=emprestimo.id,
            livro_id=emprestimo.livro_id,
            livro_titulo=emprestimo.livro.titulo if emprestimo.livro_id else None,
            nome_leitor=emprestimo.nome_leitor,
            data_emprestimo=str(emprestimo.data_emprestimo) if emprestimo.data_emprestimo else None,
            data_devolucao=str(emprestimo.data_devolucao) if emprestimo.data_devolucao else None,
            devolvido=emprestimo.devolvido,
        )

    @staticmethod
    def to_entity(dados: dict, instancia: Emprestimo = None) -> Emprestimo:
        instancia = instancia or Emprestimo()
        instancia.livro_id = dados.get('livro_id') or dados.get('livro')
        instancia.nome_leitor = dados.get('nome_leitor')
        return instancia

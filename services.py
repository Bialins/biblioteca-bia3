
from datetime import date

from .repositories import (
    AutorRepository,
    CategoriaRepository,
    LivroRepository,
    EmprestimoRepository,
)
from .mappers import (
    AutorMapper,
    CategoriaMapper,
    LivroMapper,
    EmprestimoMapper,
)
from .exceptions import LivroJaEmprestadoException, EmprestimoJaDevolvidoException


class AutorService:

    def __init__(self):
        self.repository = AutorRepository()

    def listar(self):
        autores = self.repository.find_all()
        return [AutorMapper.to_dto(a) for a in autores]

    def buscar_por_id(self, autor_id):
        autor = self.repository.find_by_id(autor_id)
        return AutorMapper.to_dto(autor)

    def criar(self, dados: dict):
        autor = AutorMapper.to_entity(dados)
        autor = self.repository.save(autor)
        return AutorMapper.to_dto(autor)

    def atualizar(self, autor_id, dados: dict):
        autor = self.repository.find_by_id(autor_id)
        autor = AutorMapper.to_entity(dados, instancia=autor)
        autor = self.repository.save(autor)
        return AutorMapper.to_dto(autor)

    def remover(self, autor_id):
        autor = self.repository.find_by_id(autor_id)
        self.repository.delete(autor)


class CategoriaService:

    def __init__(self):
        self.repository = CategoriaRepository()

    def listar(self):
        categorias = self.repository.find_all()
        return [CategoriaMapper.to_dto(c) for c in categorias]

    def buscar_por_id(self, categoria_id):
        categoria = self.repository.find_by_id(categoria_id)
        return CategoriaMapper.to_dto(categoria)

    def criar(self, dados: dict):
        categoria = CategoriaMapper.to_entity(dados)
        categoria = self.repository.save(categoria)
        return CategoriaMapper.to_dto(categoria)

    def atualizar(self, categoria_id, dados: dict):
        categoria = self.repository.find_by_id(categoria_id)
        categoria = CategoriaMapper.to_entity(dados, instancia=categoria)
        categoria = self.repository.save(categoria)
        return CategoriaMapper.to_dto(categoria)

    def remover(self, categoria_id):
        categoria = self.repository.find_by_id(categoria_id)
        self.repository.delete(categoria)


class LivroService:

    def __init__(self):
        self.repository = LivroRepository()

    def listar(self):
        livros = self.repository.find_all()
        return [LivroMapper.to_dto(l) for l in livros]

    def buscar_por_id(self, livro_id):
        livro = self.repository.find_by_id(livro_id)
        return LivroMapper.to_dto(livro)

    def criar(self, dados: dict):
        livro = LivroMapper.to_entity(dados)
        livro = self.repository.save(livro)
        return LivroMapper.to_dto(self.repository.find_by_id(livro.id))

    def atualizar(self, livro_id, dados: dict):
        livro = self.repository.find_by_id(livro_id)
        livro = LivroMapper.to_entity(dados, instancia=livro)
        livro = self.repository.save(livro)
        return LivroMapper.to_dto(self.repository.find_by_id(livro.id))

    def remover(self, livro_id):
        livro = self.repository.find_by_id(livro_id)
        self.repository.delete(livro)


class EmprestimoService:

    def __init__(self):
        self.repository = EmprestimoRepository()
        self.livro_repository = LivroRepository()

    def listar(self):
        emprestimos = self.repository.find_all()
        return [EmprestimoMapper.to_dto(e) for e in emprestimos]

    def buscar_por_id(self, emprestimo_id):
        emprestimo = self.repository.find_by_id(emprestimo_id)
        return EmprestimoMapper.to_dto(emprestimo)

    def criar(self, dados: dict):
        livro_id = dados.get('livro_id') or dados.get('livro')

        self.livro_repository.find_by_id(livro_id)

        if self.repository.existe_emprestimo_ativo_para_livro(livro_id):
            raise LivroJaEmprestadoException(
                "Este livro já está emprestado e ainda não foi devolvido."
            )

        emprestimo = EmprestimoMapper.to_entity(dados)
        emprestimo = self.repository.save(emprestimo)
        return EmprestimoMapper.to_dto(self.repository.find_by_id(emprestimo.id))

    def devolver(self, emprestimo_id):
        emprestimo = self.repository.find_by_id(emprestimo_id)

        if emprestimo.devolvido:
            raise EmprestimoJaDevolvidoException(
                "Este empréstimo já foi devolvido anteriormente."
            )

        emprestimo.devolvido = True
        emprestimo.data_devolucao = date.today()
        emprestimo = self.repository.save(emprestimo)
        return EmprestimoMapper.to_dto(emprestimo)


from .models import Autor, Categoria, Livro, Emprestimo
from .exceptions import RecursoNaoEncontradoException


class AutorRepository:

    def find_all(self):
        return Autor.objects.all()

    def find_by_id(self, autor_id):
        try:
            return Autor.objects.get(id=autor_id)
        except Autor.DoesNotExist:
            raise RecursoNaoEncontradoException(f"Autor {autor_id} não encontrado.")

    def save(self, autor: Autor) -> Autor:
        autor.save()
        return autor

    def delete(self, autor: Autor):
        autor.delete()


class CategoriaRepository:

    def find_all(self):
        return Categoria.objects.all()

    def find_by_id(self, categoria_id):
        try:
            return Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            raise RecursoNaoEncontradoException(
                f"Categoria {categoria_id} não encontrada."
            )

    def save(self, categoria: Categoria) -> Categoria:
        categoria.save()
        return categoria

    def delete(self, categoria: Categoria):
        categoria.delete()


class LivroRepository:

    def find_all(self):
        return Livro.objects.select_related('autor', 'categoria').all()

    def find_by_id(self, livro_id):
        try:
            return Livro.objects.select_related(
                'autor', 'categoria'
            ).get(id=livro_id)
        except Livro.DoesNotExist:
            raise RecursoNaoEncontradoException(f"Livro {livro_id} não encontrado.")

    def save(self, livro: Livro) -> Livro:
        livro.save()
        return livro

    def delete(self, livro: Livro):
        livro.delete()


class EmprestimoRepository:

    def find_all(self):
        return Emprestimo.objects.select_related('livro').all()

    def find_by_id(self, emprestimo_id):
        try:
            return Emprestimo.objects.select_related('livro').get(id=emprestimo_id)
        except Emprestimo.DoesNotExist:
            raise RecursoNaoEncontradoException(
                f"Empréstimo {emprestimo_id} não encontrado."
            )

    def existe_emprestimo_ativo_para_livro(self, livro_id) -> bool:
        return Emprestimo.objects.filter(
            livro_id=livro_id,
            devolvido=False
        ).exists()

    def save(self, emprestimo: Emprestimo) -> Emprestimo:
        emprestimo.save()
        return emprestimo

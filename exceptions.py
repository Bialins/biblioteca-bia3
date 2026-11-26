class BibliotecaException(Exception):
    """Exceção base para regras de negócio da biblioteca."""
    status_code = 400

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class RecursoNaoEncontradoException(BibliotecaException):
    status_code = 404


class LivroJaEmprestadoException(BibliotecaException):
    status_code = 409  


class EmprestimoJaDevolvidoException(BibliotecaException):
    status_code = 409
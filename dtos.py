
from dataclasses import dataclass
from typing import Optional
import uuid


@dataclass
class AutorDTO:
    id: Optional[uuid.UUID]
    nome: str
    nacionalidade: Optional[str] = None


@dataclass
class CategoriaDTO:
    id: Optional[uuid.UUID]
    nome: str
    descricao: Optional[str] = None


@dataclass
class LivroDTO:
    id: Optional[uuid.UUID]
    titulo: str
    isbn: str
    autor_id: uuid.UUID
    autor_nome: Optional[str] = None
    categoria_id: Optional[uuid.UUID] = None
    categoria_nome: Optional[str] = None


@dataclass
class EmprestimoDTO:
    id: Optional[uuid.UUID]
    livro_id: uuid.UUID
    livro_titulo: Optional[str]
    nome_leitor: str
    data_emprestimo: Optional[str]
    data_devolucao: Optional[str]
    devolvido: bool

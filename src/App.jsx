
import { useState } from 'react';
import api from './services/api';

function App() {
  const [livros, setLivros] = useState([]);
  const [titulo, setTitulo] = useState('');
  const [isbn, setIsbn] = useState('');
  const [autorId, setAutorId] = useState('');
  const [categoriaId, setCategoriaId] = useState('');
  const [mensagem, setMensagem] = useState('');

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  async function fazerLogin() {
    const resposta = await api.post('/api/token/', {
      username,
      password
    });

    localStorage.setItem('access', resposta.data.access);

    api.defaults.headers.common['Authorization'] =
      `Bearer ${resposta.data.access}`;
  }

  async function listarLivros() {
    const resposta = await api.get('/api/v1/livros');
    setLivros(resposta.data);
  }

  async function cadastrarLivro(e) {
    e.preventDefault();

    try {
      await api.post('/api/v1/livros', {
        titulo,
        isbn,
        autor_id: autorId,
        categoria_id: categoriaId
      });

      setMensagem('Livro cadastrado com sucesso!');
      setTitulo('');
      setIsbn('');
      setAutorId('');
      setCategoriaId('');
      await listarLivros();
    } catch (erro) {
      setMensagem('Erro ao cadastrar livro.');
    }
  }

  return (
    <div>
      <h1>Biblioteca</h1>

      <h2>Autenticação</h2>

      <input
        placeholder="Usuário"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={fazerLogin}>Entrar</button>

      <h2>Cadastrar Livro</h2>

      <form onSubmit={cadastrarLivro}>
        <input
          placeholder="Título"
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
          required
        />

        <input
          placeholder="ISBN"
          value={isbn}
          onChange={(e) => setIsbn(e.target.value)}
          required
        />

        <input
          placeholder="ID do autor"
          value={autorId}
          onChange={(e) => setAutorId(e.target.value)}
          required
        />

        <input
          placeholder="ID da categoria"
          value={categoriaId}
          onChange={(e) => setCategoriaId(e.target.value)}
          required
        />

        <button type="submit">Cadastrar Livro</button>
      </form>

      <p>{mensagem}</p>

      <h2>Livros cadastrados</h2>

      <button onClick={listarLivros}>Listar Livros</button>

      <ul>
        {livros.map((livro) => (
          <li key={livro.id}>
            {livro.titulo} - {livro.isbn}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

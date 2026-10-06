class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"ISBN: {livro.isbn}")
            print("----------------")


livro1 = Livro("Dom Casmurro", "Machado de Assis", "123")
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", "456")

biblioteca = Biblioteca("Biblioteca Central")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

biblioteca.remover_livro(livro1)

print("Depois da remoção:")
biblioteca.listar_livros()
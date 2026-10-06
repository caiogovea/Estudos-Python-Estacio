class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aumentar_preco(self, valor):
        self.preco += valor

produto = Produto("Teclado", 100)

produto.aumentar_preco(20)
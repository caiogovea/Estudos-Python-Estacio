class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aumentar_preco(self, valor):
        self.preco += valor

    def mostrar(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco}")


produto = Produto("Teclado", 100)

produto.mostrar()

produto.aumentar_preco(20)

produto.mostrar()
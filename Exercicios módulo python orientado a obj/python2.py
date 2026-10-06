class Animal:
    def falar(self):
        print("O animal está fazendo um som.")

    def mover(self):
        print("O animal está se movendo.")


class Cachorro(Animal):
    def falar(self):
        print("Au au!")

    def mover(self):
        print("O cachorro está correndo.")


class Gato(Animal):
    def falar(self):
        print("Miau!")

    def mover(self):
        print("O gato está andando.")


cachorro = Cachorro()
gato = Gato()

cachorro.falar()
cachorro.mover()

gato.falar()
gato.mover()
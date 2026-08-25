import tkinter as tk

def clicar():
    print("Botão pressionado")

janela = tk.Tk()

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=clicar
)

botao.pack()

janela.mainloop()
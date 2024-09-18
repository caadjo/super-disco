import tkinter as tk
from tkinter import ttk
import gui.Crud1 as Crud1
import gui.Crud2 as Crud2
import gui.Crud3 as Crud3


def abrir_crud1():
    root.destroy()
    Crud1.abrir_janela_crud1()


def abrir_crud2():
    root.destroy()
    Crud2.abrir_janela_crud2()

def abrir_crud3():
    root.destroy()
    Crud3.abrir_janela_crud3()


root = tk.Tk()
root.title("MainScreen")
root.geometry("600x400")
root.configure(bg='#2e2e2e')

menu_bar = tk.Menu(root)


menu_operacao = tk.Menu(menu_bar, tearoff=0)
menu_operacao.add_command(label="Opção 1", command=abrir_crud1)
menu_operacao.add_command(label="Opção 2", command=abrir_crud2)
menu_operacao.add_command(label="Opção 3", command=abrir_crud3)


menu_bar.add_cascade(label="Operação", menu=menu_operacao)


root.config(menu=menu_bar)


frame = ttk.Frame(root, style="TFrame")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


label_operacao = ttk.Label(frame, text="Escolha uma operação no menu", style="TLabel")
label_operacao.pack(pady=20)

root.mainloop()

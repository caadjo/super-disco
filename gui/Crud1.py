import tkinter as tk

def abrir_janela_crud1():
    janela_crud1 = tk.Tk()
    janela_crud1.title("CRUD 1")
    janela_crud1.geometry("300x200")

    label = tk.Label(janela_crud1, text="Bem-vindo ao CRUD 1")
    label.pack(pady=20)

    janela_crud1.mainloop()

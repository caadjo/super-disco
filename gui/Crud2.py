import tkinter as tk

def abrir_janela_crud2():
    janela_crud2 = tk.Tk()
    janela_crud2.title("CRUD 2")
    janela_crud2.geometry("300x200")

    label = tk.Label(janela_crud2, text="Bem-vindo ao CRUD 2")
    label.pack(pady=20)

    janela_crud2.mainloop()

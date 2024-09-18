import tkinter as tk

def abrir_janela_crud3():
    janela_crud3 = tk.Tk()
    janela_crud3.title("CRUD 3")
    janela_crud3.geometry("300x200")

    label = tk.Label(janela_crud3, text="Bem-vindo ao CRUD 3")
    label.pack(pady=20)

    janela_crud3.mainloop()

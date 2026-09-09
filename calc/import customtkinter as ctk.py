import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

calculadora = ctk.CTk()
calculadora.title("Calculadora")
calculadora.geometry("320x420")
calculadora.resizable(False, False)

# Cabeçalho roxo
janela = ctk.CTkFrame(calculadora, width=320, height=60, fg_color="#4c487a")
janela.grid(row=0, column=0)
janela.grid_propagate(False)

# Área dos botões com imagem de fundo
numerico = ctk.CTkFrame(calculadora, width=320, height=360, fg_color="transparent")
numerico.grid(row=1, column=0)
numerico.grid_propagate(False)

# Imagem de fundo
imagem = Image.open(r"C:\Users\Fab\Documents\Projetos\tungtung.png")
imagem = imagem.resize((320, 360))
foto = ImageTk.PhotoImage(imagem)
fundo = ctk.CTkLabel(numerico, image=foto, text="")
fundo.place(x=0, y=0)

# Botões transparentes
b1 = ctk.CTkButton(numerico, text="C", width=100, height=50,
                   fg_color="transparent", hover_color="#4c487a",
                   text_color="white", border_width=0)
b1.place(x=0, y=0)

b2 = ctk.CTkButton(numerico, text="%", width=70, height=50,
                   fg_color="transparent", hover_color="#4c487a",
                   text_color="white", border_width=0)
b2.place(x=110, y=0)

b3 = ctk.CTkButton(numerico, text="/", width=70, height=50,
                   fg_color="transparent", hover_color="#4c487a",
                   text_color="white", border_width=0)
b3.place(x=184, y=0)

calculadora.mainloop()
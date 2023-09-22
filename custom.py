import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("green")

class Segund():
    def principal(self):
        while True:
            self.t = customtkinter.CTk()
            self.janela.destroy()
            self.config_screen1()
            self.t.mainloop()
    def config_screen1(self):
        self.t.geometry('1200x600')
        self.t.title('JRMADEIRAS')
        self.t.configure(bg="green")
        self.t.resizable(False, False)
        self.t.iconbitmap("commit/jr.icon.ico")
        
janela = customtkinter.CTk()


class MyApp(Segund):
    def __init__(self):
        self.janela = janela
        self.config_screen()
        self.images()
        self.create_label()
        self.janela.mainloop()
    
    def config_screen(self):
        self.janela.geometry('1000x600')
        self.janela.title('JRMADEIRAS')
        self.janela.configure(bg="green")
        self.janela.maxsize(1000,600)
        self.janela.iconbitmap("commit/jr.icon.ico")
#janela.resizable(False, False)
    def images(self):
        self.img = PhotoImage(file='commit/logo.png')
        self.frame1 = Frame(self.janela, bg="green")
        self.frame1.place(relx=0.00, rely=0.00, relwidth=0.99, relheight=0.+20)
    def create_label(self):
        self.labe_image = customtkinter.CTkLabel(self.frame1,text='',image=self.img)
        self.labe_image.place(relx=0.10, rely=0.01)

        self.frame = customtkinter.CTkFrame(self.janela, width=439, height=600)
        self.frame.place(relx=0.56, rely=0.00)

        self.labe = customtkinter.CTkLabel(self.frame, text="SCANNER", text_color='#008000',font=('Roboto',30,"bold"))
        self.labe.place(relx=0.28, rely=0.15)



        entry_name = customtkinter.CTkEntry(self.frame, placeholder_text="Digite seu email:", width=300)
        entry_name.place(relx=0.12, rely=0.30)

        entry_pass = customtkinter.CTkEntry(self.frame, placeholder_text="Digite sua senha:", width=300)
        entry_pass.place(relx=0.12, rely=0.40)

        check = customtkinter.CTkCheckBox(self.frame, text="Lembrar-me da proxima vez")
        check.place(relx=0.12, rely=0.50)

        button = customtkinter.CTkButton(self.frame, text="Logar", width=200, command=self.principal)
        button.place(relx=0.20, rely=0.60)


MyApp()
from tkinter import *
import qrcode
from PIL import Image, ImageDraw
from tkinter import messagebox
import random

main = Tk()

class func():
    def gera_qr_code(self):
        url = self.entrada.get()
        url2 = random.randint(1, 1000)

        if len(url) == 0:
            messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma URL válida")
        else:
            opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é: \n "
                    f"Endereço: {url} \n "
                    f"Pronto para salvar?")

        if opcao_escolhida:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save(f'qrExport{url2}.png')

class Aplicacao(func):

    def __init__(self):
        self.root = main
        self.tela()
        self.frametela()
        self.componetes()
        self.root.mainloop()

    def tela(self):
        self.root.title("Gerar QRCode")
        self.root.geometry("600x400")

    def frametela(self):
        self.frame = Frame(self.root, bg="#55002F")
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)


    def componetes(self):
        self.label = Label(self.frame, text='Insira o endereço', )
        self.label.place(relx=0.43, rely=0.4)

        self.entrada = Entry(self.frame)
        self.entrada.place(relx=0.2, rely=0.5, relheight=0.075, relwidth=0.7)

        self.butao = Button(text='Gerar', command=self.gera_qr_code)
        self.butao.place(relx=0.48, rely=0.6)

Aplicacao()


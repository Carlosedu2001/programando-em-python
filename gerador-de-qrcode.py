import qrcode
import os

os.system("cls")

link = input(str("Digite o link para gerar o QR code: "))
nome = input(str("Digite o nome que deseja salvar este QR code: "))

imagem_qrcode = qrcode.make(link)
imagem_qrcode.save(f"{nome}.png")
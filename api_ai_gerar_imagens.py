import os
import openai

os.system("cls")

secret = input("Digite sua chave para validação: ")

openai.api_key = secret
openai.Model.list()

request = input("Digite o que deseja: ")

imagem = openai.Image.create(
    prompt = request,
    n = 1,
    size = "256x256"
)

print(f"\n{imagem['data'][0]['url']}")
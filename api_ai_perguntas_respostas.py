import os
import openai

os.system("cls")

secret = input("Digite sua chave para validação: ")

up = '\033[F'

openai.api_key = secret
openai.Model.list()

prompt = input("Digite o que deseja: ")

response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)

print(f'{up}{response["choices"][0]["text"]}')
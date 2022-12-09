import os, requests

os.system("cls")

def poke_habilidades(poke):

    os.system("cls")
    print(f"Habilidades do Pokémon {pokemon.title()}:\n")

    for i in poke['abilities']:
        print(i['ability']['name'])

def main():
    global pokemon
    pokemon = str(input("Digite qual Pokémon deseja acessar as habilidades: "))
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")
    poke = res.json()
    poke_habilidades(poke)

main()
import requests

def get_pokemons(url="http://pokeapi.co/api/v2/pokemon-form/", offset=0):
	args={"offset":offset} if offset else {}
	respuesta=requests.get(url, params=args)
	if respuesta.status_code == 200:
		payload = respuesta.json()
		results = payload.get("results",[])
		if results:
			for pokemon in results:
				name = pokemon["name"]
				print(name)
		next = input("¿Continuar listando? [Y/N]").lower()
		if next == "y":
			get_pokemons(offset=offset+20)
		
url="http://pokeapi.co/api/v2/pokemon-form/"
get_pokemons()
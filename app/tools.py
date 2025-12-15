import requests


def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    return requests.get(url).json()



import requests

def consultar_pokemon(nome_ou_id: str) -> dict:
    url = f"https://pokeapi.co/api/v2/pokemon/{str(nome_ou_id).strip().lower()}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()

        tipos = [t["type"]["name"] for t in data.get("types", [])]
        habilidades = [a["ability"]["name"] for a in data.get("abilities", [])]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data.get("stats", [])}

        resultado = {
            "nome": data.get("name"),             
            "id": data.get("id"),
            "tipos": tipos,
            "habilidades": habilidades,
            "altura": data.get("height"),          
            "peso": data.get("weight"),            
            "experiencia_base": data.get("base_experience"),
            "stats": stats,
            "sprite": data.get("sprites", {}).get("front_default")
        }
        return resultado
    except requests.HTTPError as e:
        return {"erro": f"Pokémon não encontrado: {nome_ou_id}", "detalhes": str(e)}
    except Exception as e:
        return {"erro": "Falha ao consultar PokéAPI", "detalhes": str(e)}

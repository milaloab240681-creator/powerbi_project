import requests

def get_pokemon_types():
    # Usamos la PokéAPI oficial, que no bloquea las GitHub Actions
    url = "https://pokeapi.co/api/v2/type"
    
    print("Conectando de forma segura con pokeapi.co...")
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Error al acceder a la API: {response.status_code}")
            return

        data = response.json()
        types = set()
        
        # Recorremos los resultados que nos devuelve el JSON de la API
        for result in data.get("results", []):
            name = result.get("name")
            # Filtramos "unknown" y "shadow" que son tipos internos/especiales del juego
            if name and name not in ["unknown", "shadow"]:
                types.add(name.capitalize())

        # Guardamos los resultados en el archivo para el repositorio
        output_file = "pokemon_types.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("=== TIPOS DE POKÉMON ENCONTRADOS (OFICIALES) ===\n")
            for p_type in sorted(types):
                f.write(f"- {p_type}\n")
                
        print(f"¡Éxito! Se han extraído {len(types)} tipos y se han guardado en {output_file}")

    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")

if __name__ == "__main__":
    get_pokemon_types()

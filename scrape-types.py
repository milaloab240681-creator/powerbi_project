import requests
from bs4 import BeautifulSoup

def get_pokemon_types():
    # URL de la sección de tipos en la Fandom de Pokémon
    url = "https://pokemon.fandom.com/wiki/Types"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print("Conectando con pokemon.fandom.com...")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error al acceder a la web: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscamos los enlaces que apuntan a los tipos elementales
    # En la wiki suelen estar estructurados dentro de tablas de clases específicas o elementos de lista
    types = set()
    
    # Estrategia: Buscar elementos que contengan "/wiki/Type" en sus enlaces de manera limpia
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Filtramos para quedarnos solo con los tipos principales (ej: /wiki/Water_type)
        if "/wiki/" in href and "_type" in href.lower() and not any(x in href.lower() for x in ["category:", "user:", "talk:"]):
            # Extraemos el nombre del tipo limpiando el formato de la URL
            type_name = href.split('/')[-1].replace('_type', '').replace('_Type', '')
            if type_name and type_name.isalpha():
                types.add(type_name.capitalize())

    print("\n=== TIPOS DE POKÉMON ENCONTRADOS ===")
    for p_type in sorted(types):
        print(f"- {p_type}")

if __name__ == "__main__":
    get_pokemon_types()

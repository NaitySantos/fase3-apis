import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    return resposta.json()

def buscar_coordenadas(cidade):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt"
    resposta = requests.get(url)
    dados = resposta.json()
    if dados["results"]:
        lat = dados["results"][0]["latitude"]
        lon = dados["results"][0]["longitude"]
        return lat, lon
    return None, None

def buscar_clima(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    resposta = requests.get(url)
    return resposta.json()

def main():
    cep = input("Digite o CEP: ")
    resultado = buscar_cep(cep)

    print("\nEndereco encontrado!")
    print("CEP:", resultado["cep"])
    print("Logradouro:", resultado["logradouro"])
    print("Bairro:", resultado["bairro"])
    print("Cidade:", resultado["localidade"])
    print("UF:", resultado["uf"])

    cidade = resultado["localidade"]
    lat, lon = buscar_coordenadas(cidade)

    clima = buscar_clima(lat, lon)
    temperatura = clima["current_weather"]["temperature"]

    print("\nClima em", cidade)
    print("Temperatura:", temperatura, "C")

if __name__ == "__main__":
    main()
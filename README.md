# Consultor de CEP e Clima

Sistema em Python que busca endereco completo pelo CEP e retorna a temperatura atual da cidade.

## O que o sistema faz
- Busca endereco completo a partir do CEP informado
- Localiza as coordenadas geograficas da cidade automaticamente
- Retorna a temperatura atual em tempo real

## Tecnologias
- Python 3
- API ViaCEP - consulta de enderecos
- API Open-Meteo - consulta de clima
- API Open-Meteo Geocoding - coordenadas geograficas

## Como usar
1. Clone o repositorio
2. Instale as dependencias: pip install requests
3. Rode: python consultor.py
4. Digite o CEP quando solicitado

## Exemplo de uso
Digite o CEP: 01310100

Endereco encontrado!
CEP: 01310-100
Logradouro: Avenida Paulista
Bairro: Bela Vista
Cidade: Sao Paulo
UF: SP

Clima em Sao Paulo
Temperatura: 24.5 C

from faker import Faker
import json
import random

faker = Faker('pt-BR')

dados = []

# Criando arquivos usuarios
auth_user = {"model":"auth.User", "pk":1, "fields": {
    "password": "pbkdf2_sha256$870000$rpBoWLRUyt4VmmJS8X28gp$4BAZ2l4g2TyeRa9iQOWPbnco0Gh/VkGa7Qo7nAOChNg=",
    "is_superuser": True,
    "username": "leonardo",
    "is_staff": True,
    "is_active": True
}}
dados.append(auth_user)

# Criando arquivos testes para model tipo
contador = 0
for _ in range(3):
    
    contador += 1

    tipo = {"model":"pindorama.Tipos", "pk":contador, "fields": {
        "tipo": faker.text(max_nb_chars=10),
        "descricao": faker.text(max_nb_chars=200),
        "data_criacao": faker.date()
    }}
    dados.append(tipo)

# Criando arquivos testes para model formas
contador = 0
for _ in range(10):

    contador += 1

    forma = {"model":"pindorama.Formas", "pk":contador, "fields": {
        "forma": faker.text(max_nb_chars=15),
        "descricao": faker.text(max_nb_chars=200),
        "data_criacao": faker.date()
    }}
    dados.append(forma)

# Criando arquivos testes para model origens
contador = 0
for _ in range(10):

    contador += 1

    origem = {"model":"pindorama.Origens", "pk":contador, "fields": {
        "origem": faker.text(max_nb_chars=20),
        "descricao": faker.text(max_nb_chars=200),
        "data_criacao": faker.date()
    }}
    dados.append(origem)

# Criando arquivos testes para model criaturas
contador = 0
for _ in range(10):

    contador += 1

    criatura = {"model":"pindorama.Criaturas", "pk":contador, "fields": {
        "criatura": faker.text(max_nb_chars=15),
        "tipo": random.randint(1, 3),
        "forma": random.randint(1, 10),
        "origem": random.randint(1, 10),
        "foto_perfil": r"semimagem/semimage.jpg",
        "descricao": faker.text(max_nb_chars=200),
        "data_criacao": faker.date()
    }}
    dados.append(criatura)

# Criando arquivos testes para model album
contador = 0
for _ in range(10):

    contador += 1

    album = {"model": "pindorama.AlbumCriaturas", "pk":contador, "fields": {
        "criatura": random.randint(1,10),
        "foto": r"semimagem/semimage.jpg",
        "fonte": faker.text(max_nb_chars=20),
        "data_criacao": faker.date()
    }}
    dados.append(album)

# Criando arquivos testes para model lendas
contador = 0
for _ in range(10):

    contador += 1

    lendas = {"model": "pindorama.LendasCriaturas", "pk":contador, "fields": {
        "criatura": random.randint(1,10),
        "titulo": faker.text(max_nb_chars=15),
        "estoria": faker.text(max_nb_chars=500),
        "fonte": faker.text(max_nb_chars=20),
        "data_criacao": faker.date()
    }}
    dados.append(lendas)

with open('dados_teste.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print('Arquivo de dados testes gerado com sucesso!')
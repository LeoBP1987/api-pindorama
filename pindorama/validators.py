import re

def nome_invalido(nome):
    return not re.match(r"^[A-Za-zÀ-ÿ]+$", nome)
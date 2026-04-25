import pytest
from faker import Faker
import unicodedata
import re

fake = Faker('pt_BR')

def nome_limpo():
    nome = f"{fake.first_name()} {fake.last_name()}"

    nome = unicodedata.normalize('NFD', nome)
    nome = ''.join(c for c in nome if unicodedata.category(c) != 'Mn')
    nome = re.sub(r"[^a-zA-Z\s]", "", nome)
    nome = " ".join(nome.split())

    return nome[:50]


def email_limpo(nome):
    # gera email baseado no nome (mais realista)
    base = nome.lower().replace(" ", ".")
    return f"{base}@teste.com"


def documento_limpo():
    # CPF só números
    return re.sub(r"\D", "", fake.cpf())


def telefone_limpo():
    # só números
    return re.sub(r"\D", "", fake.phone_number())


def tratar(valor):
    if valor in ["vazio", "null", "None"]:
        return ""
    return valor


@pytest.fixture
def paciente():
    nome = nome_limpo()

    return {
        "nome": nome,
        "email": email_limpo(nome),
        "documento": documento_limpo(),
        "telefone": telefone_limpo()
    }
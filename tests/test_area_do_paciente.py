from src.pages.area_do_paciente_page import AreaPaciente
from src.utils.dados_paciente import tratar
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../src/features/area_do_paciente.feature")

@given("que o paciente está logado")
def paciente_logado(admin_logado):
    pass

@given("que o paciente está na área do paciente")
def paciente_na_area(admin_logado):
    AreaPaciente(admin_logado.page).acessar_area_paciente()

@when("acessar a área do paciente")
def acessar_area(login_page):
    paciente = AreaPaciente(login_page.page)
    paciente.acessar_area_paciente()

@when(parsers.parse('informar senha atual "{senha_atual}"'))
def informar_senha_atual(admin_logado, senha_atual):
    area = AreaPaciente(admin_logado.page)
    senha_atual = tratar(senha_atual)
    area.preencher_senha_atual(senha_atual)

@when(parsers.parse('informar nova senha "{nova_senha}"'))
def informar_nova_senha(admin_logado, nova_senha):
    area = AreaPaciente(admin_logado.page)
    nova_senha = tratar(nova_senha)
    area.preencher_nova_senha(nova_senha)

@when('clicar em "Atualizar senha"')
def clicar_atualizar(admin_logado):
    area = AreaPaciente(admin_logado.page)
    area.clicar_atualizar()

@then(parsers.parse('o sistema deve exibir os dados "{nome}" "{email}" "{sexo}"'))
def validar_dados(login_page, nome, email, sexo):
    area = AreaPaciente(login_page.page)
    area.validar_dados_paciente(nome, email, sexo)

@then(parsers.parse('o sistema deve exibir mensagem "{mensagem}"'))
def validar_mensagem(admin_logado, mensagem):
    area = AreaPaciente(admin_logado.page)
    area.validar_mensagem(mensagem)


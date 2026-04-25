from src.pages.login_paciente_page import LoginPaciente
from playwright.sync_api import expect
from src.utils.dados_paciente import tratar
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../src/features/login_paciente.feature")


@given("que o paciente está na tela de login")
def acessar_tela(login_page):
    login_page.acessar_home()
    expect(login_page.page).to_have_title("Sistema Hospitalar")

@when(parsers.parse('informar email "{email}" e senha "{senha}"'))
def informar_login(login_page, email, senha):

    email = tratar(email)
    senha = tratar(senha)

    login_page.preencher_email(email)
    login_page.preencher_senha(senha)


@when('clicar no botão "Entrar"')
def clicar_entrar(login_page):
    login_page.clicar_entrar()

@then("o sistema deve autenticar o usuário")
def autenticar_usuario(page):
    login = LoginPaciente(page)
    login.validar_login_sucesso("ADMINISTRADOR")

@then(parsers.parse('o sistema deve exibir a mensagem "{mensagem}"'))
def validar_mensagem(login_page, mensagem):
    login_page.validar_mensagem_erro(mensagem)


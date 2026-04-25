from src.pages.cadastro_paciente_page import CadastroPaciente
from playwright.sync_api import expect
from src.utils.dados_paciente import paciente, tratar
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../src/features/cadastro_paciente.feature")

@given("que estou na tela de cadastro de paciente")
def acessar_tela(page):
    cadastro_paciente = CadastroPaciente(page)
    cadastro_paciente.acessar_cadastro()
    expect(page.get_by_role("heading", name="Cadastro")).to_be_visible()


@when("preencher dados válidos do paciente")
def preencher_dados(page, paciente):
    cadastro = CadastroPaciente(page)

    cadastro.realizar_cadastro(
        nome=paciente["nome"],
        email=paciente["email"],
        sexo="Masculino",
        cpf=paciente["documento"],
        telefone=paciente["telefone"],
        senha="Senha123"
    )

@when(parsers.parse('preencher "{nome}" "{email}" "{sexo}" "{cpf}" "{telefone}" "{senha}"'))
def preencher(page, nome, email, sexo, cpf, telefone, senha):
    cadastro = CadastroPaciente(page)

    cadastro.realizar_cadastro(
        nome=tratar(nome),
        email=tratar(email),
        sexo=tratar(sexo),
        cpf=tratar(cpf),
        telefone=tratar(telefone),
        senha=tratar(senha)
    )

@when('clicar no botão "Cadastrar"')
def clicar_cadastrar(page):
    cadastro = CadastroPaciente(page)
    cadastro.botao_cadastrar.click()

@then("devo validar a mensagem de cadastro realizado")
def validar_cadastro(page):
    expect(page.get_by_text("Cadastro realizado com sucesso")).to_be_visible()


@then(parsers.parse('o sistema deve exibir a mensagem "{mensagem}"'))
def validar_mensagem(page, mensagem):
    expect(page.get_by_text(mensagem)).to_be_visible()

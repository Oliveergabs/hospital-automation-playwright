from openpyxl.worksheet import page
from pytest_bdd import scenarios, given, when, then, parsers
from src.pages.consulta_telemedicina_page import Telemedicina


scenarios("../src/features/consulta_telemedicina.feature")


@given("que o paciente está na tela de telemedicina", target_fixture="tela_telemedicina")
def tela_telemedicina(admin_logado):
    page = admin_logado.page

    tela = Telemedicina(page)
    tela.acessar_consulta_telemedicina()
    return tela

@given("possui uma consulta agendada")
def possuir_consulta(tela_telemedicina):
    tela_telemedicina.agendar_consulta_valida()

@when(parsers.parse('informar a especialidade "{especialidade}"'))
def informar_especialidade(tela_telemedicina, especialidade):
    tela_telemedicina.selecionar_especialidade(especialidade)


@when(parsers.parse('informar o médico "{medico}"'))
def informar_medico(tela_telemedicina, medico):
    tela_telemedicina.selecionar_medico(medico)


@when(parsers.parse('informar a data "{data}"'))
def informar_data(tela_telemedicina, data):
    if data == "futuro":
        data = tela_telemedicina.data_futura()
    tela_telemedicina.informar_data(data)

@when(parsers.parse('informar o horário "{hora}"'))
def informar_hora(tela_telemedicina, hora):
    tela_telemedicina.selecionar_hora(hora)

@when('clicar em "Agendar"')
def clicar_agendar(tela_telemedicina):
    tela_telemedicina.clicar_agendar()

@when('clicar em "Cancelar"')
def clicar_cancelar(tela_telemedicina):
    tela_telemedicina.cancelar_consulta()

@when('clicar em "Cancelar" e não confirmar')
def cancelar_sem_confirmar(tela_telemedicina):
    tela_telemedicina.cancelar_consulta_e_nao_confirmar()

@when('clicar em "Entrar na consulta"')
def clicar_entrar(tela_telemedicina):
    tela_telemedicina.entrar_na_consulta()

@then(parsers.parse('o sistema deve exibir mensagem "{mensagem}"'))
def validar_mensagem(tela_telemedicina, mensagem):
    tela_telemedicina.validar_mensagem(mensagem)

@then("a consulta deve aparecer na lista")
def validar_lista(tela_telemedicina):
    assert tela_telemedicina.consulta_aparece_na_lista()

@then("a consulta deve ser removida da lista")
def validar_remocao(tela_telemedicina):
    tela_telemedicina.validar_consulta_removida()

@then("o sistema deve direcionar para a sala de consulta")
def validar_entrada(tela_telemedicina):
    tela_telemedicina.validar_entrada_consulta()

@then("a consulta deve permanecer na lista")
def validar_permanece(tela_telemedicina):
    tela_telemedicina.validar_consulta_na_lista()
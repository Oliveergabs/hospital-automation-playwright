from pytest_bdd import scenarios, given, when, then, parsers
from src.pages.consulta_presencial_page import Consulta

scenarios("../src/features/consulta_presencial.feature")


@given("que o paciente está na tela de consulta", target_fixture="tela_consulta")
def acessar_consulta(admin_logado):
    page = admin_logado.page
    page.evaluate("localStorage.clear()")  # 👈 AQUI

    tela = Consulta(page)
    tela.acessar_consulta_presencial()
    return tela

@given("que o paciente possui uma consulta agendada")
def possuir_consulta(tela_consulta):
    tela_consulta.agendar_consulta_valida()

@when(parsers.parse('informar a especialidade "{especialidade}"'))
def informar_especialidade(tela_consulta, especialidade):
    if especialidade != "vazio":
        tela_consulta.selecionar_especialidade(especialidade)

@when(parsers.parse('informar o médico "{medico}"'))
def informar_medico(tela_consulta, medico):
    if medico != "vazio":
        tela_consulta.selecionar_medico(medico)

@when(parsers.parse('informar a data "{data}"'))
def informar_data(tela_consulta, data):
    if data == "futuro":
        data = tela_consulta.data_futura()

    if data != "vazio":
        tela_consulta.informar_data(data)

@when(parsers.parse('informar o horário "{hora}"'))
def informar_hora(tela_consulta, hora):
    if hora != "vazio":
        tela_consulta.selecionar_hora(hora)

@when('clicar em "Agendar"')
def clicar_agendar(tela_consulta):
    tela_consulta.clicar_agendar()

@when('clicar em "Cancelar"')
def cancelar_consulta(tela_consulta):
    tela_consulta.cancelar_consulta()

@when('clicar em "Cancelar" e não confirmar')
def cancelar_sem_confirmar(tela_consulta):
    tela_consulta.cancelar_consulta_e_nao_confirmar()

@then(parsers.parse('o sistema deve exibir mensagem "{mensagem}"'))
def validar_mensagem(tela_consulta, mensagem):
    tela_consulta.validar_mensagem(mensagem)

@then("a consulta deve aparecer na lista")
def validar_lista(tela_consulta):
    tela_consulta.validar_consulta_na_lista()

@then("a consulta deve ser removida da lista")
def validar_remocao(tela_consulta):
    tela_consulta.validar_consulta_removida()

@then("a consulta deve permanecer na lista")
def validar_permanece(tela_consulta):
    tela_consulta.validar_consulta_na_lista()
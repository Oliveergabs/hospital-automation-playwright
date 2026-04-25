from src.pages.base_page import BasePage
from datetime import datetime, timedelta

class Consulta(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.select_especialidade = "#especialidade"
        self.select_medico = "#medico"
        self.input_data = "#data"
        self.btn_agendar = "button:has-text('Agendar')"
        self.btn_cancelar = "#cancelarConsulta"
        self.msg = "#msgConsulta"
        self.lista_consultas = "#listaConsultas"

    # =========================
    # NAVEGAÇÃO
    # =========================

    def acessar_consulta_presencial(self):
        self.menu_consulta.click()

    # =========================
    # AÇÕES
    # =========================

    def selecionar_especialidade(self, especialidade):
        self.page.select_option(self.select_especialidade, label=especialidade)

    def selecionar_medico(self, medico):
        self.page.wait_for_selector(self.select_medico)
        self.page.select_option(self.select_medico, label=medico)

    def informar_data(self, data):
        self.page.fill(self.input_data, data)

    def selecionar_hora(self, hora):
        self.page.locator(".horarios button", has_text=hora).click()

    def clicar_agendar(self):
        self.page.click(self.btn_agendar)

    # =========================
    # REUTILIZAÇÃO
    # =========================

    def agendar_consulta_valida(self):
        self.selecionar_especialidade("Clínico Geral")
        self.selecionar_medico("Dr. João Silva")

        data = self.data_futura()
        self.informar_data(data)

        self.selecionar_hora("14:00")
        self.clicar_agendar()

    # =========================
    # CANCELAMENTO
    # =========================

    def cancelar_consulta(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.locator(self.btn_cancelar).first.click()

    def cancelar_consulta_e_nao_confirmar(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.locator(self.btn_cancelar).first.click()

    # =========================
     # VALIDAÇÕES
     # =========================

    def validar_mensagem(self, mensagem):
        self.page.wait_for_selector(self.msg, state="visible")
        texto = self.page.inner_text(self.msg)

        print("Mensagem exibida:", texto)

        assert mensagem in texto

    def validar_consulta_na_lista(self):
        self.page.wait_for_selector(self.lista_consultas)
        assert self.page.locator(self.lista_consultas).is_visible()

    def validar_consulta_removida(self):
        self.page.wait_for_selector("text=Nenhuma consulta agendada")
        assert self.page.locator("text=Nenhuma consulta agendada").is_visible()

    # =========================
    # UTIL
    # =========================

    def data_futura(self, dias=5):
        return (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%d")
from src.pages.base_page import BasePage
from datetime import datetime, timedelta

class Telemedicina(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # Seletores
        self.select_especialidade = "#especialidade"
        self.select_medico = "#medicoTele"
        self.input_data = "#data"
        self.input_hora = "#hora"
        self.btn_agendar = "button:has-text('Agendar')"
        self.btn_cancelar = "#cancelar"
        self.btn_entrar_consulta = "button:has-text('Entrar na consulta')"
        self.msg = "#msgTele"
        self.lista_consultas = "#listaConsultas"



    def acessar_consulta_telemedicina(self):
        self.menu_telemedicina.click()

    # =========================
    # AÇÕES
    # =========================

    def selecionar_especialidade(self, especialidade):
        if especialidade and especialidade != "vazio":
            self.page.select_option(self.select_especialidade, label=especialidade)

    def selecionar_medico(self, medico):
        if medico and medico != "vazio":
            self.page.wait_for_selector(self.select_medico)

            options = self.page.locator(f"{self.select_medico} option").all_text_contents()
            print("Opções disponíveis:", options)

            self.page.select_option(self.select_medico, label=medico)

    def selecionar_hora(self, hora):
        if hora and hora != "vazio":
            btn = self.page.locator(".horarios button", has_text=hora)

            if btn.is_enabled():
                btn.click()
            else:
                print(f"Horário {hora} está desabilitado")

    def clicar_agendar(self):
        self.page.click(self.btn_agendar)

    def consulta_aparece_na_lista(self):
        return self.page.locator(self.lista_consultas).is_visible()


    def informar_data(self, data):
        if data == "vazio":
            return

        if data == "futuro":
            data = self.data_futura()
        else:
            data = self.formatar_data(data)

        self.page.fill("#data", data)

    # ================================
    # REUTILIZAÇÃO
    # ================================

    def agendar_consulta_valida(self):
        self.page.select_option("#especialidade", label="Cardiologia")
        self.page.select_option("#medicoTele", label="Dra. Ana Costa")

        # data futura no formato correto (YYYY-MM-DD)
        data = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")

        self.page.fill("#data", data)

        self.page.locator(".horarios button", has_text="14:00").click()

        self.page.click(self.btn_agendar)

    # ================================
    # CANCELAMENTO DE CONSULTA
    # ================================

    def cancelar_consulta(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

        self.page.locator(self.btn_cancelar).first.click()

    def cancelar_consulta_e_nao_confirmar(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())

        self.page.locator(self.btn_cancelar).first.click()

    # =========================
    # ENTRAR NA SALA DE TELECONSULTA
    #==========================

    def entrar_na_consulta(self):
        self.page.click(self.btn_entrar_consulta)

    # =========================
    # VALIDAÇÕES
    # =========================

    def validar_mensagem(self, mensagem):
        self.page.wait_for_selector(self.msg, state="attached")
        texto = self.page.inner_text(self.msg)

        print("Mensagem exibida:", texto)

        assert mensagem in texto

    def validar_consulta_removida(self):
        self.page.wait_for_selector("text=Nenhuma consulta agendada")
        assert self.page.locator("text=Nenhuma consulta agendada").is_visible()

    def validar_entrada_consulta(self):
        self.page.wait_for_selector("text=Sala de consulta")
        assert self.page.locator("text=Sala de consulta").is_visible()

    def validar_consulta_na_lista(self):
        self.page.wait_for_selector(self.lista_consultas)
        assert self.page.locator(self.lista_consultas).is_visible()


    # =========================
    # UTIL
    # =========================
    def data_futura(self, dias=5):
        return (datetime.now() + timedelta(days=dias)).strftime("%d/%m/%Y")

    def formatar_data(self, data):
        # recebe 25/04/2026 → vira 2026-04-25
        if not data:
            return ""
        dia, mes, ano = data.split("/")
        return f"{ano}-{mes}-{dia}"

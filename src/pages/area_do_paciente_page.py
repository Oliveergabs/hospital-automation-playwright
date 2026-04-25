from src.pages.base_page import BasePage
from playwright.sync_api import expect


class AreaPaciente(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.nome = page.get_by_text("Nome:")
        self.email = page.get_by_text("Email:")
        self.cpf = page.get_by_text("CPF:")
        self.sexo = page.get_by_text("Sexo:")

        self.senha_atual = page.locator("#senhaAtual")
        self.nova_senha = page.locator("#novaSenha")
        self.botao_atualizar = page.get_by_role("button", name="Atualizar senha")

    def acessar_area_paciente(self):
        self.menu_paciente.click()

    def validar_dados_paciente(self, nome, email, sexo):
        expect(self.page.get_by_text(f"Nome: {nome}")).to_be_visible()
        expect(self.page.get_by_text(f"Email: {email}")).to_be_visible()
        expect(self.page.get_by_text(f"Sexo: {sexo}")).to_be_visible()

    def preencher_senha_atual(self, senha):
        self.senha_atual.fill(senha)

    def preencher_nova_senha(self, senha):
        self.nova_senha.fill(senha)

    def clicar_atualizar(self):
        self.botao_atualizar.click()

    def validar_mensagem(self, mensagem):
        expect(self.page.get_by_text(mensagem)).to_be_visible()
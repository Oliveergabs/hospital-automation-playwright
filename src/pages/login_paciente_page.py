from src.pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPaciente(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.input_email_login = page.get_by_role("textbox", name="Email")
        self.input_senha_login = page.get_by_role("textbox", name="Senha")
        self.botao_entrar = page.get_by_role("button", name="Entrar")

    def efetuar_login(self, email, senha):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_entrar()

    def preencher_email(self, email):
        self.input_email_login.fill(email)

    def preencher_senha(self, senha):
        self.input_senha_login.fill(senha)

    def clicar_entrar(self):
        self.botao_entrar.click()

    def validar_login_sucesso(self, usuario):
        expect(self.page.locator("#userNome")).to_have_text(usuario)

    def validar_mensagem_erro(self, mensagem):
        expect(self.page.locator(f"text={mensagem}")).to_be_visible()
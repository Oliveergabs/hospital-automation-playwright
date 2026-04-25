from src.pages.base_page import BasePage
class CadastroPaciente(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.input_nome_cadastro = page.get_by_role("textbox", name="Digite o nome completo")
        self.input_email_cadastro = page.get_by_role("textbox", name="Digite o email")
        self.select_sexo =  page.locator("#sexo")
        self.input_cpf_cadastro = page.get_by_role("textbox", name="Digite o CPF")
        self.input_telefone_cadastro = page.locator("#telefone")
        self.input_senha_cadastro = page.get_by_role("textbox", name="Crie uma senha")
        self.botao_cadastrar = page.get_by_role("button", name="Cadastrar")

    def realizar_cadastro(self, nome='', email='', sexo='', cpf='', telefone='', senha=''):

        if nome:
            self.input_nome_cadastro.fill(nome)

        if email:
            self.input_email_cadastro.fill(email)

        if sexo:
            self.select_sexo.select_option(label=sexo)

        if cpf:
            self.input_cpf_cadastro.fill(cpf)

        if telefone:
            self.input_telefone_cadastro.fill(telefone)

        if senha:
            self.input_senha_cadastro.fill(senha)
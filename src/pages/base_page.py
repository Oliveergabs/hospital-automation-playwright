
class BasePage:
    def __init__(self, page):
        self.page = page
        self.menu_paciente = page.get_by_text("Área do paciente Visualize")
        self.menu_consulta =  page.get_by_text("Consulta presencial Agende")
        self.menu_telemedicina = page.get_by_text("Telemedicina Consulta")


    def acessar_home(self):
        self.page.goto('')

    def acessar_cadastro(self):
        self.page.goto('pages/cadastro.html')
        self.page.wait_for_load_state("domcontentloaded")


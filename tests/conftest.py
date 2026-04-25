import os

import pytest
import pytest_html
from slugify import slugify

from src.pages.login_paciente_page import LoginPaciente
from src.pages.consulta_telemedicina_page import Telemedicina
from src.pages.consulta_presencial_page import Consulta

STORAGE_FILE = 'tests/playwright/auth/state.json'

@pytest.fixture
def login_page(page):
    return LoginPaciente(page)

@pytest.fixture
def admin_logado(login_page):
    login_page.acessar_home()
    login_page.efetuar_login("admin@hospital.com", "Admin123")
    login_page.validar_login_sucesso("ADMINISTRADOR")
    return login_page

@pytest.fixture
def tela_telemedicina(page):
    return Telemedicina(page)

@pytest.fixture
def tela_consulta(page):
    return Consulta(page)

@pytest.fixture(scope='session')
def contexto(browser):
    if os.path.isfile(STORAGE_FILE):
        contexto = browser.new_context(
            base_url='http://localhost:8006/',
            record_video_dir='reports/videos',
            storage_state=STORAGE_FILE
        )
    else:
        contexto = browser.new_context(
            base_url='http://localhost:8006/',
            record_video_dir='reports/videos',
        )
    contexto.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield contexto

    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
    contexto.tracing.stop(path='reports/trace/trace.zip')
    if not os.path.isfile(STORAGE_FILE):
        contexto.storage_state(path=STORAGE_FILE)

    contexto.close()


@pytest.fixture(scope='session')
def page(contexto):
    pagina = contexto.new_page()
    pagina.set_default_timeout(10000)
    pagina.set_default_navigation_timeout(30000)
    yield pagina
    pagina.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Este hook é executado após cada fase do teste.
    Usamos ele para verificar falhas e anexar capturas de tela ao relatório HTML.
    """
    outcome = yield
    report = outcome.get_result()

    # Lista de extras para o relatório HTML
    extras = getattr(report, 'extra', [])

    # Só captura na fase 'call' (execução do teste em si)
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')

        try:
            # Captura quando falha (mas não é um XFAIL esperado)
            if (report.skipped and xfail) or (report.failed and not xfail):

                # Garante nome de arquivo seguro
                screen_file = f"imagens/{slugify(item.nodeid)}.png"

                # page deve estar disponível no teste (fixture do Playwright)
                page = item.funcargs.get("page")

                if page:
                    page.screenshot(path=screen_file, full_page=True)
                    extras.append(pytest_html.extras.png(screen_file))

        except Exception as e:
            print(f"Erro ao capturar imagem: {e}")

    report.extra = extras
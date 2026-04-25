# language: pt

# Project: Automação sistema hospitalar
# Description: BDD para automação de testes do modulo de login
# Author: Gabriel Henrique de Oliveira


Funcionalidade: Login de paciente
  Como um paciente
  Eu quero realizar login na aplicação
  Para poder agendar consultas

  Este fluxo valida o acesso do paciente ao sistema,
  garantindo que as credenciais informadas estejam corretas,
  permitindo o uso das funcionalidades, como o agendamento de consultas.

  @smoke @login
  Cenário: Login com sucesso
    Dado que o paciente está na tela de login
    Quando informar email "admin@hospital.com" e senha "Admin123"
    E clicar no botão "Entrar"
    Então o sistema deve autenticar o usuário

  @smoke @login
  Esquema do Cenário: Validação de login
    Dado que o paciente está na tela de login
    Quando informar email "<email>" e senha "<senha>"
    E clicar no botão "Entrar"
    Então o sistema deve exibir a mensagem "<mensagem>"

  Exemplos:
    | email              | senha     | mensagem                    |
    | admin@hospital.com | Admin     | Credenciais inválidas       |
    | adm@hospital.com   | Admin123  | Credenciais inválidas       |
    | vazio              | vazio     | Preencha todos os campos    |


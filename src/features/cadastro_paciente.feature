# language: pt

# Project: Automação sistema hospitalar
# Description: BDD para automação de testes do modulo de cadastro
# Author: Gabriel Henrique de Oliveira


Funcionalidade: Cadastro de paciente
  Como um atendente
  Eu quero cadastrar um paciente
  Para que ele possa ser atendido

  Este fluxo valida o cadastro de pacientes com dados válidos,
  garantindo que as informações obrigatórias sejam preenchidas
  corretamente e que o sistema confirme o cadastro com sucesso.



  @smoke @cadastro
  Cenário: Cadastrar paciente
    Dado que estou na tela de cadastro de paciente
    Quando preencher dados válidos do paciente
    E clicar no botão "Cadastrar"
    Então devo validar a mensagem de cadastro realizado


  @smoke  @cadastro
  Esquema do Cenário: Validação de campos obrigatórios
    Dado que estou na tela de cadastro de paciente
    Quando preencher "<nome>" "<email>" "<sexo>" "<cpf>" "<telefone>" "<senha>"
    E clicar no botão "Cadastrar"
    Então o sistema deve exibir a mensagem "<mensagem>"

  Exemplos:
    | nome              | email               | sexo      | cpf         | telefone          | senha     | mensagem                               |
    | vazio             | gabriel@teste.com   | Masculino | 12345678900 | 11987654321       | Senha123  | Preencha todos os campos obrigatórios! |
    | Gabriel Oliveira  | vazio               | Masculino | 12345678900 | 21991234567       | Senha123  | Preencha todos os campos obrigatórios! |
    | Lucas Ferreira    | lucas@teste.com     | vazio     | 12345678900 | 31999887766       | Senha123  | Preencha todos os campos obrigatórios! |
    | Rafael Souza      | rafael@teste.com    | Masculino | vazio       | 41995554433       | Senha123  | Preencha todos os campos obrigatórios! |
    | Mariana Costa     | mariana@teste.com   | Feminino  | 12345678900 | 51992223344       | vazio     | Preencha todos os campos obrigatórios! |

  @smoke @cadastro
  Esquema do Cenário: Validação de email inválido
    Dado que estou na tela de cadastro de paciente
    Quando preencher "<nome>" "<email>" "<sexo>" "<cpf>" "<telefone>" "<senha>"
    E clicar no botão "Cadastrar"
    Então o sistema deve exibir a mensagem "<mensagem>"

  Exemplos:
    | nome             | email              | sexo      | cpf         | telefone    | senha     | mensagem         |
    | Gabriel Oliveira | gabrielteste.com   | Masculino | 12345678900 | 11987654321 | Senha123  | Email inválido!  |
    | Mariana Costa    | @teste.com         | Feminino  | 12345678900 | 21991234567 | Senha123  | Email inválido!  |
    | Gabriel Oliveira | gabriel@           | Masculino | 12345678900 | 31999887766 | Senha123  | Email inválido!  |

  @smoke @cadastro
  Esquema do Cenário: Validação de CPF inválido
    Dado que estou na tela de cadastro de paciente
    Quando preencher "<nome>" "<email>" "<sexo>" "<cpf>" "<telefone>" "<senha>"
    E clicar no botão "Cadastrar"
    Então o sistema deve exibir a mensagem "<mensagem>"

  Exemplos:
    | nome             | email              | sexo      | cpf         | telefone    | senha     | mensagem        |
    | Gabriel Oliveira | gabriel@teste.com  | Masculino | 123         | 11999999999 | Senha123  | CPF inválido!   |
    | Gabriel Oliveira | gabriel@teste.com  | Masculino | 11111111111 | 11999999999 | Senha123  | CPF inválido!   |
    | Mariana Costa    | mariana@teste.com  | Feminino  | abcdefghijk | 11999999999 | Senha123  | CPF inválido!   |
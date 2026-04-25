# language: pt

# Project: Automação sistema hospitalar
# Description: BDD para automação de testes no modulo Telemedicina
# Author: Gabriel Henrique de Oliveira


Funcionalidade: Telemedicina
  Como um paciente
  Eu quero agendar e acessar consultas online
  Para realizar atendimentos médicos à distância

  Este fluxo valida o agendamento de consultas de telemedicina,
  garantindo que não seja possível selecionar datas ou horários passados,
  especialmente quando o agendamento for para o dia atual.

  Além disso, valida que os dados informados sejam obrigatórios,
  que o agendamento seja armazenado corretamente,
  permitindo sua visualização na lista de consultas agendadas.

  O fluxo também permite o acesso à sala de consulta,
  simulando o atendimento remoto de forma rápida e prática.

  @smoke @telemedicina
  Cenário: Consulta deve aparecer na lista após agendamento
    Dado que o paciente está na tela de telemedicina
    Quando informar a especialidade "Cardiologia"
    E informar o médico "Dra. Ana Costa"
    E informar a data "futuro"
    E informar o horário "14:00"
    E clicar em "Agendar"
    Então o sistema deve exibir mensagem "Consulta agendada com sucesso!"
    E a consulta deve aparecer na lista

  @smoke @telemedicina
  Esquema do Cenário: Validação de agendamento de telemedicina
    Dado que o paciente está na tela de telemedicina
    Quando informar a especialidade "<especialidade>"
    E informar o médico "<medico>"
    E informar a data "<data>"
    E informar o horário "<hora>"
    E clicar em "Agendar"
    Então o sistema deve exibir mensagem "<mensagem>"

  Exemplos:
    | especialidade | medico          | data        | hora  | mensagem                                           |
    | Clínico Geral | vazio           | futuro      | 10:00 | Preencha todos os campos!                          |
    | Clínico Geral | Dr. João Silva  | vazio       | 10:00 | Preencha todos os campos!                          |
    | Clínico Geral | Dr. João Silva  | futuro      | vazio | Preencha todos os campos!                          |

  @smoke @telemedicina
  Cenário: Cancelar consulta agendada
    Dado que o paciente está na tela de telemedicina
    E possui uma consulta agendada
    Quando clicar em "Cancelar"
    Então a consulta deve ser removida da lista

  @smoke @telemedicina
  Cenário: Não cancelar consulta ao fechar popup
    Dado que o paciente está na tela de telemedicina
    E possui uma consulta agendada
    Quando clicar em "Cancelar" e não confirmar
    Então a consulta deve permanecer na lista

  @smoke @telemedicina
  Cenário: Entrar na sala de telemedicina
    Dado que o paciente está na tela de telemedicina
    Quando clicar em "Entrar na consulta"
    Então o sistema deve direcionar para a sala de consulta
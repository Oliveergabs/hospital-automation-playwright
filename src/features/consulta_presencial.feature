# language: pt

# Project: Automação sistema hospitalar
# Description: BDD para automação de testes no modulo Consultas
# Author: Gabriel Henrique de Oliveira


Funcionalidade: Consulta
  Como paciente
  Quero agendar consultas presenciais
  Para ser atendido na unidade

  Este fluxo valida o agendamento de consultas de presenciais,
  garantindo que não seja possível selecionar datas ou horários passados,
  especialmente quando o agendamento for para o dia atual.

  Além disso, valida que os dados informados sejam obrigatórios,
  que o agendamento seja armazenado corretamente,
  permitindo sua visualização na lista de consultas agendadas.

  @smoke @consulta
  Cenário: Agendar consulta com sucesso
    Dado que o paciente está na tela de consulta
    Quando informar a especialidade "Clínico Geral"
    E informar o médico "Dr. João Silva"
    E informar a data "futuro"
    E informar o horário "10:00"
    E clicar em "Agendar"
    Então o sistema deve exibir mensagem "Consulta agendada com sucesso!"
    E a consulta deve aparecer na lista

  @smoke @consulta
  Esquema do Cenário: Validação de agendamento de consulta
    Dado que o paciente está na tela de consulta
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

  @smoke @consulta
  Cenário: Cancelar consulta agendada
    Dado que o paciente possui uma consulta agendada
    Quando clicar em "Cancelar"
    Então a consulta deve ser removida da lista

  @smoke @consulta
  Cenário: Não cancelar consulta ao fechar popup
    Dado que o paciente possui uma consulta agendada
    Quando clicar em "Cancelar" e não confirmar
    Então a consulta deve permanecer na lista
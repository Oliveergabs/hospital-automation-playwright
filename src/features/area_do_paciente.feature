# language: pt

# Project: Automação sistema hospitalar
# Description: BDD para automação de testes do modulo Area do paciente
# Author: Gabriel Henrique de Oliveira


Funcionalidade: Área do paciente
  Como um paciente
  Eu quero acessar minha área no sistema
  Para visualizar meus dados e gerenciar minha conta

  Este fluxo valida o acesso à área do paciente,
  garantindo que as informações do usuário sejam exibidas corretamente,
  além de permitir ações como a alteração de senha,
  validando também regras de negócio como campos obrigatórios e consistência dos dados.

  @smoke @paciente
  Esquema do Cenário: Exibir dados do paciente
    Dado que o paciente está logado
    Quando acessar a área do paciente
    Então o sistema deve exibir os dados "<nome>" "<email>" "<sexo>"

  Exemplos:
    | nome           | email                | sexo      |
    | Administrador  | admin@hospital.com   | Masculino |

  @smoke @paciente
  Esquema do Cenário: Validação de alteração de senha
    Dado que o paciente está na área do paciente
    Quando informar senha atual "<senha_atual>"
    E informar nova senha "<nova_senha>"
    E clicar em "Atualizar senha"
    Então o sistema deve exibir mensagem "<mensagem>"

  Exemplos:
   | senha_atual | nova_senha   | mensagem                      |
   | vazio       | Nova123      | Preencha todos os campos      |
   | Admin123    | vazio        | Preencha todos os campos      |
   | Admin12     | 123          | Senha atual incorreta!        |
   | Admin123    | admin        | Senha deve conter no mínimo 8 caracteres, com maiúscula, minúscula e número! |
   | Admin123    | Senha1020    | Senha atualizada com sucesso! |
// =========================
// VALIDAÇÕES
// =========================
function validarEmail(email) {
  return /\S+@\S+\.\S+/.test(email);
}

function validarSenha(senha) {
  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(senha);
}

function validarCPF(cpf) {
  cpf = cpf.replace(/[^\d]+/g, '');
  if (cpf.length !== 11) return false;
  if (/^(\d)\1+$/.test(cpf)) return false;

  let soma = 0;
  for (let i = 0; i < 9; i++) {
    soma += parseInt(cpf.charAt(i)) * (10 - i);
  }

  let resto = (soma * 10) % 11;
  if (resto === 10) resto = 0;
  if (resto !== parseInt(cpf.charAt(9))) return false;

  soma = 0;
  for (let i = 0; i < 10; i++) {
    soma += parseInt(cpf.charAt(i)) * (11 - i);
  }

  resto = (soma * 10) % 11;
  if (resto === 10) resto = 0;

  return resto === parseInt(cpf.charAt(10));
}

// =========================
// NAVEGAÇÃO
// =========================
function irCadastro() {
  window.location.href = "/pages/cadastro.html";
}

function voltarLogin() {
  window.location.href = "/index.html";
}

function logout() {
  localStorage.removeItem("usuarioLogado"); // 🔥 limpa sessão
  window.location.href = "/index.html";
}

function irConsulta() {
  window.location.href = "/pages/consulta.html";
}

function irTelemedicina() {
  window.location.href = "/pages/telemedicina.html";
}

function irPaciente() {
  window.location.href = "/pages/paciente.html";
}

function irHome() {
  window.location.href = "/pages/home.html";
}

// =========================
// TOGGLE SENHA 👁️
// =========================
function toggleSenha(id) {
  const input = document.getElementById(id);
  input.type = input.type === "password" ? "text" : "password";
}

// =========================
// LOGIN
// =========================
function login() {
  const email = document.getElementById("email").value;
  const senha = document.getElementById("senha").value;
  const erro = document.getElementById("erro");

  erro.innerText = "";

  if (!email || !senha) {
    erro.innerText = "Preencha todos os campos!";
    return;
  }

  if (!validarEmail(email)) {
    erro.innerText = "Email inválido!";
    return;
  }

  const usuarioSalvo = JSON.parse(localStorage.getItem("usuario"));

  // 🔥 ADMIN (opcional)
  if (email === "admin@hospital.com" && senha === "Admin123") {

    const admin = {
      nome: "Administrador",
      email: "admin@hospital.com",
      cpf: "000.000.000-00",
      sexo: "Masculino",
      senha: "Admin123"
    };

    localStorage.setItem("usuarioLogado", JSON.stringify(admin));
    window.location.href = "/pages/home.html";
    return;
  }

  // 🔥 USUÁRIO NORMAL (sempre senha atualizada)
  if (
    usuarioSalvo &&
    email === usuarioSalvo.email &&
    senha === usuarioSalvo.senha
  ) {
    localStorage.setItem("usuarioLogado", JSON.stringify(usuarioSalvo));
    window.location.href = "/pages/home.html";
  } else {
    erro.innerText = "Credenciais inválidas!";
  }
}

function getUsuarioLogado() {
  const data = localStorage.getItem("usuarioLogado");
  return data ? JSON.parse(data) : null;
}

function carregarUsuarioNavbar() {
  const usuario = getUsuarioLogado();

  if (!usuario) return;

  const nome = usuario.nome.split(" ")[0].toUpperCase();

  const el = document.getElementById("userNome");
  if (el) {
    el.innerText = nome;
  }
}

window.onload = function () {
  carregarUsuarioNavbar();
};

// =========================
// CADASTRO
// =========================
function cadastrar() {
  const nome = document.getElementById("nome").value;
  const email = document.getElementById("email").value;
  const cpf = document.getElementById("cpf").value;
  const telefone = document.getElementById("telefone").value;
  const senha = document.getElementById("senha").value;
  const sexo = document.getElementById("sexo").value;
  const msg = document.getElementById("msg");

  msg.innerText = "";

  if (!nome || !email || !cpf || !senha || !sexo) {
    msg.style.color = "red";
    msg.innerText = "Preencha todos os campos obrigatórios!";
    return;
  }

  if (!validarEmail(email)) {
    msg.style.color = "red";
    msg.innerText = "Email inválido!";
    return;
  }

  if (!validarCPF(cpf)) {
    msg.style.color = "red";
    msg.innerText = "CPF inválido!";
    return;
  }

  if (!validarSenha(senha)) {
    msg.style.color = "red";
    msg.innerText =
      "Senha deve ter no mínimo 8 caracteres, com letra maiúscula, minúscula e número!";
    return;
  }

  const usuario = {
    nome,
    email,
    cpf,
    telefone,
    senha,
    sexo
  };

  localStorage.setItem("usuario", JSON.stringify(usuario));

  msg.style.color = "green";
  msg.innerText = "Cadastro realizado com sucesso!";

  setTimeout(() => {
    window.location.href = "/index.html";
  }, 1500);
}

// =========================
// ALTERAR SENHA
// =========================
function alterarSenha() {
  const senhaAtual = document.getElementById("senhaAtual").value;
  const novaSenha = document.getElementById("novaSenha").value;
  const msg = document.getElementById("msgSenha");

  const senhaAtualInput = senhaAtual.value;
  const novaSenhaInput = novaSenha.value;

  let usuario = JSON.parse(localStorage.getItem("usuarioLogado"));

  msg.innerText = "";

  if (!senhaAtual || !novaSenha) {
    msg.style.color = "red";
    msg.innerText = "Preencha todos os campos!";

    setTimeout(() => {
      msg.innerText = "";
    }, 3000);

    return;
  }

  if (!usuario || senhaAtual !== usuario.senha) {
    msg.style.color = "red";
    msg.innerText = "Senha atual incorreta!";

    setTimeout(() => {
      msg.innerText = "";
    }, 3000);

    return;
  }

  if (!validarSenha(novaSenha)) {
    msg.style.color = "red";
    msg.innerText =
      "Senha deve conter no mínimo 8 caracteres, com maiúscula, minúscula e número!";

    setTimeout(() => {
      msg.innerText = "";
    }, 3000);

    return;
  }

  if (senhaAtual === novaSenha) {
    msg.style.color = "red";
    msg.innerText = "A nova senha não pode ser igual à atual!";

    setTimeout(() => {
      msg.innerText = "";
    }, 3000);

    return;
  }

  // 🔥 ATUALIZA SENHA
  usuario.senha = novaSenha;

  localStorage.setItem("usuarioLogado", JSON.stringify(usuario));
  localStorage.setItem("usuario", JSON.stringify(usuario));


  msg.style.color = "green";
  msg.innerText = "Senha atualizada com sucesso!";

  // ✅ limpa campos
  senhaAtualInput.value = "";
  novaSenhaInput.value = "";

  // ✅ some mensagem depois de 3s
  setTimeout(() => {
    msg.innerText = "";
  }, 3000);
}

// CONTROLE DE HORARIO
function selecionarHora(btn) {
  // remove seleção anterior
  document.querySelectorAll(".horarios button")
    .forEach(b => b.classList.remove("active"));

  // marca o clicado
  btn.classList.add("active");

  // salva valor correto
  document.getElementById("hora").value = btn.innerText;
}

// TELEMEDICINA
// =========================
function agendarTelemedicina() {
  const especialidade = document.getElementById("especialidade").value;
  const medico = document.getElementById("medicoTele").value;
  const data = document.getElementById("data").value;
  const hora = document.getElementById("hora").value;
  const msg = document.getElementById("msgTele");

  if (!especialidade || !medico || !data || !hora) {
    msg.style.color = "red";
    msg.innerText = "Preencha todos os campos!";

    setTimeout(() => msg.innerText = "", 5000);
    return;
  }

  // pega data/hora atual
const agora = new Date();

// monta data selecionada corretamente
const [ano, mes, dia] = data.split("-");
const [horaSel, minSel] = hora.split(":");

const dataHoraSelecionada = new Date(
  ano,
  mes - 1,
  dia,
  horaSel,
  minSel
);

// valida se é passado
if (dataHoraSelecionada <= agora) {
  msg.style.color = "red";
  msg.innerText = "Não é possível agendar para horários passados!";

  setTimeout(() => msg.innerText = "", 3000);
  return;
}

  const novaConsulta = { especialidade, medico, data, hora };

  let consultas = JSON.parse(localStorage.getItem("consultasTele")) || [];

  consultas.push(novaConsulta);

  localStorage.setItem("consultasTele", JSON.stringify(consultas));

  msg.style.color = "green";
  msg.innerText = "Consulta agendada com sucesso!";

  // 🔥 some após 3 segundos
  setTimeout(() => {
    msg.innerText = "";
  }, 5000);

  carregarConsultasTele();
}

function entrarConsulta() {
  // 🔥 SEM validação, SEM consulta, SEM condição
  window.location.href = "/pages/sala.html";
}

function toggleMic() {
  alert("Microfone ativado/desativado");
}

function toggleCam() {
  alert("Câmera ativada/desativada");
}

function sairConsulta() {
  alert("Consulta encerrada");
  window.location.href = "/pages/telemedicina.html";
}

function carregarConsultasTele() {
  const lista = document.getElementById("listaConsultas");
  const consultas = JSON.parse(localStorage.getItem("consultasTele")) || [];

  lista.innerHTML = "";

  if (consultas.length === 0) {
    lista.innerHTML = "<p>Nenhuma consulta agendada</p>";
    return;
  }

  consultas.forEach((c, index) => {
    lista.innerHTML += `
      <div class="consulta-item">
        <div>
          <strong>${c.especialidade}</strong><br>
          ${c.medico}<br> 
          ${c.data} às ${c.hora}
        </div>

        <button id="cancelar" onclick="cancelarConsultaTele(${index})">❌</button>
      </div>
    `;
  });
}

function cancelarConsultaTele(index) {
  const confirmar = confirm("Tem certeza que deseja cancelar sua consulta?");
  if (!confirmar) return;

  let consultas = JSON.parse(localStorage.getItem("consultasTele")) || [];

  consultas.splice(index, 1);

  localStorage.setItem("consultasTele", JSON.stringify(consultas));

  carregarConsultasTele();
}

function fecharModal() {
  document.getElementById("modalCancel").style.display = "none";
  indexParaCancelar = null;
}

let indexParaCancelar = null;

function confirmarCancelamento() {
  if (indexParaCancelar === null) return; // 🔥 proteção

  let consultas = JSON.parse(localStorage.getItem("consultas")) || [];

  consultas.splice(indexParaCancelar, 1);

  localStorage.setItem("consultas", JSON.stringify(consultas));

  fecharModal();
  carregarConsultasTele();
}

const medicosPorEspecialidade = {
  "Clínico Geral": ["Dr. João Silva", "Dra. Maria Souza"],
  "Cardiologia": ["Dr. Carlos Lima", "Dra. Ana Costa"],
  "Psicologia": ["Dra. Fernanda Alves"],
  "Dermatologia": ["Dr. Pedro Rocha"]
};

function atualizarMedicos(selectMedicoId = "medico") {
  const especialidade = document.getElementById("especialidade").value;
  const select = document.getElementById(selectMedicoId);

  if (!select) return;

  // 🔥 reset
  select.innerHTML = '<option value="">Selecione um médico</option>';

  const medicos = medicosPorEspecialidade[especialidade];

  if (!medicos) return;

  select.innerHTML = '<option value="">Selecione um médico</option>';

  medicos.forEach(medico => {
    const option = document.createElement("option");
    option.value = medico;
    option.textContent = medico;
    select.appendChild(option);
  });
  select.selectedIndex = 0;
}

// =========================
// CONSULTAS PRESENCIAIS
// =========================
function agendarConsulta() {
  const especialidade = document.getElementById("especialidade").value;
  const medico = document.getElementById("medico").value;
  const data = document.getElementById("data").value;
  const hora = document.getElementById("hora").value;
  const msg = document.getElementById("msgConsulta");

  if (!especialidade || !medico || !data || !hora) {
    msg.style.color = "red";
    msg.innerText = "Preencha todos os campos!";

    setTimeout(() => msg.innerText = "", 3000);
    return;
  }

  // pega data/hora atual
const agora = new Date();

// monta data selecionada corretamente
const [ano, mes, dia] = data.split("-");
const [horaSel, minSel] = hora.split(":");

const dataHoraSelecionada = new Date(
  ano,
  mes - 1,
  dia,
  horaSel,
  minSel
);

// valida se é passado
if (dataHoraSelecionada <= agora) {
  msg.style.color = "red";
  msg.innerText = "Não é possível agendar para horários passados!";

  setTimeout(() => msg.innerText = "", 3000);
  return;
}

  const novaConsulta = {
    especialidade,
    medico,
    data,
    hora
  };

  let consultas = JSON.parse(localStorage.getItem("consultasPresenciais")) || [];

  consultas.push(novaConsulta);

  localStorage.setItem("consultasPresenciais", JSON.stringify(consultas));

  msg.style.color = "green";
  msg.innerText = "Consulta agendada com sucesso!";
   setTimeout(() => {
    msg.innerText = "";
  }, 3000);

  carregarConsultasPresenciais();
}

function carregarConsultasPresenciais() {
  const lista = document.getElementById("listaConsultas");
  console.log(lista);
  const consultas = JSON.parse(localStorage.getItem("consultasPresenciais")) || [];

  lista.innerHTML = "";

  if (consultas.length === 0) {
    lista.innerHTML = "<p style='text-align:center; color: white;'>Nenhuma consulta agendada</p>";
    return;
  }

  consultas.forEach((c, index) => {
    lista.innerHTML += `
      <div class="consulta-item">
        <div>
          <strong>${c.especialidade}</strong>
          <span>${c.medico}</span>
          <span>${c.data} às ${c.hora}</span>
        </div>

        <button id=cancelarConsulta onclick="cancelarConsultaPresencial(${index})">✖</button>
      </div>
    `;
  });
}
  document.addEventListener("DOMContentLoaded", () => {
  carregarConsultasPresenciais();
});

function cancelarConsultaPresencial(index) {
  const confirmar = confirm("Tem certeza que deseja cancelar sua consulta?");
  if (!confirmar) return;

  let consultas = JSON.parse(localStorage.getItem("consultasPresenciais")) || [];

  consultas.splice(index, 1);

  localStorage.setItem("consultasPresenciais", JSON.stringify(consultas));

  carregarConsultasPresenciais();
}

function atualizarHorarios() {
  const dataSelecionadaStr = document.getElementById("data").value;
  if (!dataSelecionadaStr) return;

  const hoje = new Date();

  // normaliza HOJE (zera hora)
  const hojeData = new Date(hoje.getFullYear(), hoje.getMonth(), hoje.getDate());

  // converte input (yyyy-mm-dd)
  const [ano, mes, dia] = dataSelecionadaStr.split("-");
  const dataSelecionada = new Date(ano, mes - 1, dia);

  const botoes = document.querySelectorAll(".horarios button");

  botoes.forEach(btn => {
    const horaBotao = parseInt(btn.innerText.split(":")[0]);
    const horaAtual = hoje.getHours();

    btn.disabled = false;

    // 🔴 DATA PASSADA → bloqueia tudo
    if (dataSelecionada < hojeData) {
      btn.disabled = true;
    }

    // 🟡 HOJE → bloqueia horários já passados
    if (dataSelecionada.getTime() === hojeData.getTime()) {
      if (horaBotao <= horaAtual) {
        btn.disabled = true;
      }
    }

    // 🧹 limpeza se desabilitou
    if (btn.disabled) {
      btn.classList.remove("active");

      const horaInput = document.getElementById("hora");
      if (horaInput.value === btn.innerText) {
        horaInput.value = "";
      }
    }
  });
}
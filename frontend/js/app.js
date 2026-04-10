const API = '/api';

const state = {
  alunos: [],
  termoBusca: '',
};

//  Comunicação com a API
async function fetchAlunos() {
  const res = await fetch(`${API}/alunos`);
  return res.json();
}

async function postAluno(dados) {
  const res = await fetch(`${API}/alunos`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dados),
  });
  return res.json();
}

async function putAluno(matricula, dados) {
  const res = await fetch(`${API}/alunos/${encodeURIComponent(matricula)}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dados),
  });
  return res.json();
}

async function deleteAluno(matricula) {
  await fetch(`${API}/alunos/${encodeURIComponent(matricula)}`, {
    method: 'DELETE',
  });
}

//  Carregar e renderizar
async function carregarAlunos() {
  state.alunos = await fetchAlunos();
  renderTabela();
}

function alunosFiltrados() {
  const termo = state.termoBusca.toLowerCase();
  if (!termo) return state.alunos;
  return state.alunos.filter((a) => a.nome.toLowerCase().includes(termo));
}

function renderTabela() {
  const tbody = document.getElementById('tbodyAlunos');
  const info  = document.getElementById('tableInfo');
  const lista = alunosFiltrados();
  const total = state.alunos.length;

  tbody.innerHTML = '';

  if (lista.length === 0) {
    tbody.innerHTML = `
      <tr class="row-empty">
        <td colspan="5">Nenhum aluno encontrado.</td>
      </tr>`;
    info.textContent = `Exibindo 0 de ${total} aluno(s)`;
    return;
  }

  lista.forEach((aluno) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td title="${aluno.matricula}">${aluno.matricula}</td>
      <td title="${aluno.nome}">${aluno.nome}</td>
      <td title="${aluno.curso}">${aluno.curso}</td>
      <td title="${aluno.email}">${aluno.email}</td>
      <td class="td-actions">
        <button class="btn-edit" title="Editar aluno" data-mat="${aluno.matricula}">
          <i class="bi bi-pencil-fill"></i>
        </button>
        <button class="btn-delete" title="Excluir aluno" data-mat="${aluno.matricula}">
          <i class="bi bi-trash3-fill"></i>
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });

  tbody.querySelectorAll('.btn-edit').forEach((btn) => {
    btn.addEventListener('click', () => {
      const aluno = state.alunos.find((a) => a.matricula === btn.dataset.mat);
      if (!aluno) return;
      document.getElementById('eMatricula').value = aluno.matricula;
      document.getElementById('eNome').value      = aluno.nome;
      document.getElementById('eEmail').value     = aluno.email;
      bsModalEditar.show();
    });
  });

  tbody.querySelectorAll('.btn-delete').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const aluno = state.alunos.find((a) => a.matricula === btn.dataset.mat);
      if (!aluno) return;
      if (!confirm(`Excluir o aluno "${aluno.nome}"?`)) return;
      await deleteAluno(btn.dataset.mat);
      await carregarAlunos();
    });
  });

  info.textContent = `Exibindo ${lista.length} de ${total} aluno(s)`;
}

//  Dropdown customizado
function initDropdown(wrapperId, hiddenId) {
  const wrapper = document.getElementById(wrapperId);
  const hidden  = document.getElementById(hiddenId);
  const trigger = wrapper.querySelector('.drop-trigger');
  const label   = wrapper.querySelector('.drop-selected');
  const menu    = wrapper.querySelector('.drop-menu');
  const items   = wrapper.querySelectorAll('.drop-item');

  trigger.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = wrapper.classList.contains('open');
    closeAllDropdowns();
    if (!isOpen) openDrop(wrapper, trigger, menu);
  });

  items.forEach((item) => {
    item.addEventListener('click', () => {
      items.forEach((i) => i.classList.remove('selected'));
      item.classList.add('selected');

      label.textContent = item.textContent;
      hidden.value = item.dataset.value;

      wrapper.classList.add('has-value');
      wrapper.classList.remove('drop-error');

      closeDrop(wrapper, menu);
    });
  });
}

function openDrop(wrapper, trigger, menu) {
  const rect       = trigger.getBoundingClientRect();
  const spaceBelow = window.innerHeight - rect.bottom;
  const menuHeight = Math.min(menu.scrollHeight, 220);

  wrapper.classList.toggle('drop-up', spaceBelow < menuHeight + 10);
  wrapper.classList.remove('closing');
  wrapper.classList.add('open');
}

function closeDrop(wrapper, menu) {
  if (!wrapper.classList.contains('open')) return;
  wrapper.classList.add('closing');
  menu.addEventListener('animationend', () => {
    wrapper.classList.remove('open', 'closing');
  }, { once: true });
}

function closeAllDropdowns() {
  document.querySelectorAll('.drop-wrapper.open').forEach((w) => {
    closeDrop(w, w.querySelector('.drop-menu'));
  });
}

document.addEventListener('click', closeAllDropdowns);

//  Modal Cadastrar
const formCadastro = document.getElementById('formCadastro');
const btnSalvar    = document.getElementById('btnSalvar');
const modalEl      = document.getElementById('modalCadastro');
const bsModal      = new bootstrap.Modal(modalEl);

btnSalvar.addEventListener('click', async () => {
  formCadastro.classList.add('was-validated');
  const nativeOk = formCadastro.checkValidity();

  const cursoVal = document.getElementById('fCurso').value;
  if (!cursoVal) document.getElementById('dropCurso').classList.add('drop-error');

  if (!nativeOk || !cursoVal) return;

  await postAluno({
    nome:  document.getElementById('fNome').value,
    email: document.getElementById('fEmail').value,
    curso: cursoVal,
  });

  await carregarAlunos();
  resetModalCadastro();
  bsModal.hide();
});

function resetModalCadastro() {
  formCadastro.reset();
  formCadastro.classList.remove('was-validated');

  const wrapper = document.getElementById('dropCurso');
  wrapper.classList.remove('has-value', 'drop-error', 'open', 'closing');
  wrapper.querySelector('.drop-selected').textContent = 'Selecione o curso...';
  wrapper.querySelectorAll('.drop-item').forEach((i) => i.classList.remove('selected'));
  document.getElementById('fCurso').value = '';
}

modalEl.addEventListener('hidden.bs.modal', resetModalCadastro);

//  Modal Editar
const formEditar      = document.getElementById('formEditar');
const btnSalvarEdicao = document.getElementById('btnSalvarEdicao');
const modalEditarEl   = document.getElementById('modalEditar');
const bsModalEditar   = new bootstrap.Modal(modalEditarEl);

btnSalvarEdicao.addEventListener('click', async () => {
  formEditar.classList.add('was-validated');
  if (!formEditar.checkValidity()) return;

  const matricula = document.getElementById('eMatricula').value;
  await putAluno(matricula, {
    nome:  document.getElementById('eNome').value,
    email: document.getElementById('eEmail').value,
  });

  await carregarAlunos();
  formEditar.classList.remove('was-validated');
  bsModalEditar.hide();
});

modalEditarEl.addEventListener('hidden.bs.modal', () => {
  formEditar.reset();
  formEditar.classList.remove('was-validated');
});

//  Busca do aluno
const inputBusca = document.getElementById('inputBusca');

inputBusca.addEventListener('input', () => {
  state.termoBusca = inputBusca.value;
  renderTabela();
});

document.getElementById('btnBuscar').addEventListener('click', () => {
  state.termoBusca = inputBusca.value;
  renderTabela();
});

initDropdown('dropCurso', 'fCurso');
carregarAlunos();

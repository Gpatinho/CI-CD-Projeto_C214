from src.sistema_faculdade import SistemaFaculdade


def test_atualizar_nao_muda_curso_nem_matricula():
    sistema = SistemaFaculdade()
    aluno = sistema.criar_aluno("Gui", "gui@email.com", "eng")
    matricula_original = aluno["matricula"]
    curso_original = aluno["curso"]

    sistema.atualizar_aluno(aluno["matricula"], "Carlos", "carlos@email.com")
    atualizado = sistema.buscar_aluno(matricula_original)

    assert atualizado["matricula"] == matricula_original
    assert atualizado["curso"] == curso_original


def test_criar_aluno_email_vazio():
    sistema = SistemaFaculdade()

    # não deve lançar exceção
    aluno = sistema.criar_aluno("Gui", "", "eng")

    assert aluno["email"] == ""


def test_criar_aluno_nome_com_espacos_e_acentos():
    sistema = SistemaFaculdade()
    aluno = sistema.criar_aluno("José da Silva", "jose@email.com", "eng")

    assert aluno["nome"] == "José da Silva"


def test_contador_persiste_apos_varias_criacoes():
    sistema = SistemaFaculdade()
    matriculas = set()

    for i in range(10):
        aluno = sistema.criar_aluno(f"Aluno {i}", f"aluno{i}@email.com", "eng")
        matriculas.add(aluno["matricula"])

    # todas as 10 matrículas devem ser únicas
    assert len(matriculas) == 10
    assert len(sistema.listar_alunos()) == 10


def test_listar_alunos_retorna_copia():
    sistema = SistemaFaculdade()
    sistema.criar_aluno("Gui", "gui@email.com", "eng")

    lista = sistema.listar_alunos()
    lista.clear()

    # a lista interna não deve ter sido afetada
    assert len(sistema.listar_alunos()) == 1

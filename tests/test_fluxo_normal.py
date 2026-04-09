from src.sistema_faculdade import SistemaFaculdade
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


def test_criar_aluno():
    sistema = SistemaFaculdade()
    aluno = sistema.criar_aluno("Gui", "gui@email.com", "eng")

    assert aluno["nome"] == "Gui"
    assert aluno["curso"] == "ENG"


def test_matricula_formato():
    sistema = SistemaFaculdade()
    aluno = sistema.criar_aluno("Gui", "email", "ads")

    # matricula agora é número aleatório entre 1000 e 9999
    assert aluno["matricula"].isdigit()
    assert 1000 <= int(aluno["matricula"]) <= 9999


def test_lista_vazia():
    sistema = SistemaFaculdade()
    assert sistema.listar_alunos() == []


def test_listar_com_alunos():
    sistema = SistemaFaculdade()
    sistema.criar_aluno("Gui", "email", "eng")

    assert len(sistema.listar_alunos()) == 1


def test_matriculas_unicas():
    sistema = SistemaFaculdade()
    a1 = sistema.criar_aluno("A", "a@email.com", "eng")
    a2 = sistema.criar_aluno("B", "b@email.com", "eng")

    assert a1["matricula"] != a2["matricula"]


def test_atualizar_aluno():
    sistema = SistemaFaculdade()
    aluno = sistema.criar_aluno("Gui", "gui@email.com", "eng")

    sistema.atualizar_aluno(aluno["matricula"], "Carlos", "carlos@email.com")
    atualizado = sistema.buscar_aluno(aluno["matricula"])

    assert atualizado["nome"] == "Carlos"
    assert atualizado["email"] == "carlos@email.com"


def test_deletar_aluno():
    sistema = SistemaFaculdade()
    aluno = sistema.criar_aluno("Gui", "gui@email.com", "eng")

    sistema.deletar_aluno(aluno["matricula"])

    assert sistema.buscar_aluno(aluno["matricula"]) is None
    assert len(sistema.listar_alunos()) == 0


def test_matriculas_diferentes_mesmo_curso():
    sistema = SistemaFaculdade()
    a1 = sistema.criar_aluno("Gui", "gui@email.com", "eng")
    a2 = sistema.criar_aluno("Ana", "ana@email.com", "eng")

    assert a1["matricula"] != a2["matricula"]


def test_cursos_diferentes_contadores_independentes():
    sistema = SistemaFaculdade()
    a1 = sistema.criar_aluno("Gui", "gui@email.com", "eng")
    a2 = sistema.criar_aluno("Ana", "ana@email.com", "ads")

    assert a1["matricula"] != a2["matricula"]
    assert a1["curso"] == "ENG"
    assert a2["curso"] == "ADS"


def test_buscar_aluno():
    sistema = SistemaFaculdade()
    aluno = sistema.criar_aluno("Gui", "gui@email.com", "eng")

    encontrado = sistema.buscar_aluno(aluno["matricula"])

    assert encontrado is not None
    assert encontrado["matricula"] == aluno["matricula"]
    assert encontrado["nome"] == "Gui"

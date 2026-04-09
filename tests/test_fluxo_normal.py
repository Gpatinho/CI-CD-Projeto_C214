import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sistema_faculdade import SistemaFaculdade

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
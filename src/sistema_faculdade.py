import random


class SistemaFaculdade:
    def __init__(self):
        self.alunos = []

    def gerar_matricula(self):
        return str(random.randint(1000, 9999))

    def criar_aluno(self, nome, email, curso):
        curso = curso.upper()
        matricula = self.gerar_matricula()

        aluno = {
            "nome": nome,
            "email": email,
            "curso": curso,
            "matricula": matricula
        }

        self.alunos.append(aluno)
        return aluno

    def listar_alunos(self):
        return self.alunos.copy()

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno["matricula"] == matricula:
                return aluno
        return None

    def atualizar_aluno(self, matricula, nome, email):
        aluno = self.buscar_aluno(matricula)
        if aluno:
            aluno["nome"] = nome
            aluno["email"] = email
            return True
        return False

    def deletar_aluno(self, matricula):
        aluno = self.buscar_aluno(matricula)
        if aluno:
            self.alunos.remove(aluno)
            return True
        return False
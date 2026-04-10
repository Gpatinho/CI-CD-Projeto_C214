import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from flask import Flask, request, jsonify
from flask_cors import CORS
from sistema_faculdade import SistemaFaculdade
from database import init_db, get_session, Aluno

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

sistema = SistemaFaculdade()


def sincronizar_contadores():
    with get_session() as s:
        for a in s.query(Aluno).all():
            sistema.alunos.append(a.to_dict())


@app.get('/')
def index():
    return app.send_static_file('index.html')


@app.get('/api/alunos')
def listar():
    return jsonify(sistema.listar_alunos())


@app.post('/api/alunos')
def criar():
    data = request.get_json()

    aluno_dict = sistema.criar_aluno(
        nome=data['nome'],
        email=data['email'],
        curso=data['curso'],
    )

    with get_session() as s:
        aluno = Aluno(
            matricula=aluno_dict['matricula'],
            nome=aluno_dict['nome'],
            email=aluno_dict['email'],
            curso=aluno_dict['curso'],
        )
        s.add(aluno)
        s.commit()

    return jsonify(aluno_dict), 201


@app.put('/api/alunos/<matricula>')
def atualizar(matricula):
    data = request.get_json()
    ok = sistema.atualizar_aluno(matricula, data['nome'], data['email'])
    if not ok:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    with get_session() as s:
        aluno = s.query(Aluno).filter_by(matricula=matricula).first()
        if aluno:
            aluno.nome  = data['nome']
            aluno.email = data['email']
            s.commit()

    return jsonify(sistema.buscar_aluno(matricula))


@app.delete('/api/alunos/<matricula>')
def deletar(matricula):
    sistema.deletar_aluno(matricula)

    with get_session() as s:
        s.query(Aluno).filter_by(matricula=matricula).delete()
        s.commit()

    return '', 204


if __name__ == '__main__':
    init_db()
    sincronizar_contadores()
    app.run(debug=True, port=5000, host='0.0.0.0')

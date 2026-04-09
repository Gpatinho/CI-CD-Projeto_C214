from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = "sqlite:///alunos.db"

engine = create_engine(DATABASE_URL, echo=False)


class Base(DeclarativeBase):
    pass


class Aluno(Base):
    __tablename__ = "alunos"

    matricula = Column(String,  primary_key=True)
    nome      = Column(String,  nullable=False)
    email     = Column(String,  nullable=False)
    curso     = Column(String,  nullable=False)
    periodo   = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome":      self.nome,
            "email":     self.email,
            "curso":     self.curso,
            "periodo":   self.periodo,
        }


def init_db():
    """Cria as tabelas no banco caso ainda não exista"""
    Base.metadata.create_all(engine)


def get_session():
    """Retorna uma sessão do banco."""
    return Session(engine)

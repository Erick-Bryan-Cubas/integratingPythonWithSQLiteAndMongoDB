""" 
Arquivo de configuração do banco de dados SQLAlchemy
para o desafio de projeto "Integrando Python com SQLite e MongoDB"
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///banco_dio.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                            bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()

class Clientes(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), index=True)
    cpf = Column(String(11), unique=True)
    endereco = Column(String(120), index=True)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()
        
class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(120), index=True)
    agencia = Column(String(4), index=True)
    numero = Column(String(6), index=True)
    saldo = Column(Integer, index=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))

    def __repr__(self):
        return '<Atividade {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)
    
if __name__ == '__main__':
    init_db()
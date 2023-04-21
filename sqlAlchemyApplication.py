import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address (id = {self.id}, email_address = {self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# depreciado - será removido em futuro release
print(engine.table_names())

# investiga o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    luciano = User(
        name='Luciano',
        fullname='Luciano Carvalho Buriti',
        address=[Address(email_address='lburiti@uol.com.br')]
    )

    tatiane = User(
        name='Tatiane',
        fullname='Tatiane Alves Elias Buriti',
        address=[Address(email_address='taty_buriti@hotmail.com'),
                 Address(email_address='tatiane.buriti@gmail.com')]
    )
    patrick = User(
        name='Patrick',
        fullname='Patrick Estrela',
        address=[Address(email_address='patrick@email.com')]
    )
    # enviando para o BD (persistencia de dados)
    session.add_all([luciano, tatiane, patrick])

    session.commit()
    
stmt = select(User).where(User.name.in_(["Luciano", 'Tatiane']))
print('Recuperando usuários a partir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando os endereços a partir de condição de filtragem')
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print('\nRecuperando info de maneira ordenada')
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print('\n Recuperando pelo join')
for result in session.scalars(stmt_join):
    print(result)

#print(select(User.fullname, Address.email_address).join_from(Address, User))

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print('\nExecutando statement a partir da connection')
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print('\nExecutando count')
print(select(func.count('*')).select_from(User))
for result in session.scalars(stmt_count):
    print(result)

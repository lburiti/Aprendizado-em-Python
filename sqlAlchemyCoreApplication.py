from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, create_engine, inspect, select, func, MetaData, Table, text
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory')

#metadata_obj.create_all(engine)
metadata_obj = MetaData()
user = Table(
     'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefer = Table(
     'user_prefs',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)


for table in metadata_obj.sorted_tables:
    print(table)

#metadata_obj.create_all(engine)

metadata_db_obj = MetaData()
financial_info = Table(
    'financial_info',
    metadata_db_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

print('\nInfo da tabela users')
print(user_prefer.primary_key)
print(user_prefer.constraints)

print('\nExecutando statement sql')
sql = text('select * from user')
result = engine.execute(sql)
for row in result:
    print(row)

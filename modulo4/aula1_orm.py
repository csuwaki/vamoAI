import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date
from sqlalchemy import inspect

engine = create_engine(
    "postgresql://postgres:kamisama123@localhost/gatos",
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }
)

metadata = MetaData()
cats = Table('Gato', metadata,
    Column('id_g', Integer, primary_key=True),
    Column('nome_g', String), 
    Column('raça_g', String),
    )


dogs = Table("Cachorro", metadata, 
    Column('id_c', Integer, primary_key=True),
    Column('nome_c', String), 
    Column('raça_c', String),
)

metadata.create_all(engine)

inspector = inspect(engine)
print(inspector.get_columns('Gato'))
print(inspector.get_columns('Cachorro'))
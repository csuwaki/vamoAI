import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date
from sqlalchemy import inspect

metadata = MetaData()
books = Table('book', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String), 
    Column('author', String),
    )

engine = create_engine(
    "postgresql://postgres:kamisama123@5432/postgres",
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }
)

data = Table( 
    "dados",
    metadata, 
    Column('lancamentos', Date),
    Column('ISBN', Integer, primary_key=True)
)


metadata.create_all(engine)

inspector = inspect(engine)
print(inspector.get_columns('book'))
print(inspector.get_columns('dados'))
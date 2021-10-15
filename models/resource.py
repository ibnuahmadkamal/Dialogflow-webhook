from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

resources = Table(
    'resources',meta,
    Column('Id',Integer,primary_key=True),
    Column('NamaBarang',String(100)),
    Column('Jumlah',Integer)
)
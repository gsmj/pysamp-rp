from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import pymysql  # noqa: F401

engine = create_engine(
    "mysql+pymysql://root:root@localhost/TMS-DB",
    pool_recycle=3600,
)
session = scoped_session(sessionmaker(bind=engine))


meta = MetaData(
    naming_convention={
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s'
    },
)
Base = declarative_base(metadata=meta)

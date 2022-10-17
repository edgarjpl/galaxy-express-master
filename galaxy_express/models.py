from typing import Any

from baseplate.clients.sqlalchemy import engine_from_config
from baseplate.lib.config import RawConfig
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base: Any = declarative_base()


class ExampleModel(Base):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)


# helper functions used to initialize the database
def create_schema(app_config: RawConfig) -> None:
    engine = engine_from_config(app_config, prefix="database.", echo=True)
    Base.metadata.create_all(engine)


def drop_schema(app_config: RawConfig) -> None:
    engine = engine_from_config(app_config, prefix="database.", echo=True)
    Base.metadata.drop_all(engine)

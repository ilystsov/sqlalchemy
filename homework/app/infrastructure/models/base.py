from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

from homework.app.infrastructure.config import SCHEMA_NAME

BaseModel = declarative_base(metadata=MetaData(schema=SCHEMA_NAME))
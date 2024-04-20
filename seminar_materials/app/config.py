from sqlalchemy import create_engine

SCHEMA_NAME = 'seminar'

pg_string = "postgresql+psycopg2://postgres:mypassword@localhost:5432/postgres"
ENGINE = create_engine(pg_string)
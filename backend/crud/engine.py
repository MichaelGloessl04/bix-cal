from sqlalchemy import create_engine as sql_create_engine


def create_engine(url: str, poolclass=None):
    return sql_create_engine(url, echo=True, poolclass=poolclass)

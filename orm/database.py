from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config_db import DB, load_config
from orm.models import Base

# Загружаем параметры базы данных
config_db: DB = load_config()


# Создание движка для базы данных
engine = create_engine(
    f"""postgresql+psycopg2://{config_db.db_user}:{config_db.db_password}@{config_db.db_host}:{config_db.db_port}/{config_db.db_name}""",
    echo=False,
    pool_recycle=2000,
)


def create_tables():
    """
    Функция для создания всех таблиц.
    """
    Base.metadata.create_all(engine)
    engine.echo = False

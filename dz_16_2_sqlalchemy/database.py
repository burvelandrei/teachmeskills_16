from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config_db import DB, load_config
from models import Base

config_db: DB = load_config()


engine = create_engine(
        f"""postgresql+psycopg2://{config_db.db_user}:{config_db.db_password}@{config_db.db_host}:{config_db.db_port}/{config_db.db_name}""",
        echo=True,
        pool_recycle=2000,
    )

def create_tables():
    # Base.metadata.drop_all(engine)
    # engine.echo = True
    Base.metadata.create_all(engine)
    engine.echo = True

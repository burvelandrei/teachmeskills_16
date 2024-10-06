from sqlalchemy import create_engine
from config_db import DB, load_config

config_db: DB = load_config()


def engine():
    engine = create_engine(
        f"postgresql+psycopg2://{config_db.db_user}:{config_db.db_password}@\
            {config_db.db_host}:{config_db.db_port}/{config_db.db_name}",
        echo=True,
        pool_recycle=2000,
    )
    return engine


if __name__ == "__main__":
    print(engine())

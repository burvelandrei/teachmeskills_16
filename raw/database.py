import psycopg2
from config_db import load_config, DB

config_db: DB = load_config()


def db_connection(func):
    """
    Функция декоратор для создания подключения к БД.
    """
    try:
        db_connect = psycopg2.connect(
            dbname=config_db.db_name,
            host=config_db.db_host,
            user=config_db.db_user,
            password=config_db.db_password,
            port=config_db.db_port,
            keepalives=1,
            keepalives_idle=30,
            keepalives_interval=10,
            keepalives_count=5,
        )
        db_connect.autocommit = True
        def wrapper(*args, **kwargs):
            try:
                with db_connect as conn:
                    with conn.cursor() as cur:
                        result = func(cur, *args, **kwargs)
                        return result
            except Exception as e:
                print(f"Не смог выполнить функцию - {e}")
        return wrapper
    except Exception as e:
        print(f"Не смог подключится к БД - {e}")

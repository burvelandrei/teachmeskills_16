import psycopg2
from config_db import load_config, DB


config_db: DB = load_config()


class DBConnect:
    """
    Класс для создания подключения к БД.
    """
    connection = None
    def __init__(self, host: str, dbname: str, user: str, password: str, port: int):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port

    def _create_db_connection(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            keepalives=1,
            keepalives_idle=30,
            keepalives_interval=10,
            keepalives_count=5,
        )
        self.connection.autocommit = True
        return self.connection

    def get_connection(self):
        if self.connection and not self.connection.closed:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
            except psycopg2.OperationalError:
                return self._create_db_connection()
            return self.connection
        else:
            return self._create_db_connection()


db = DBConnect(
    config_db.db_host,
    config_db.db_name,
    config_db.db_user,
    config_db.db_password,
    config_db.db_port,
)


def db_connection(func):
    """
    Функция декоратор для передачи курсора
    """

    def wrapper(*args, **kwargs):
        with db.get_connection().cursor() as cur:
            return func(cur, *args, **kwargs)

    return wrapper

import mysql.connector
from configparser import ConfigParser
from .db_handler_config import DbAccess


class Connection():
    def __init__(self, logging):
        self.logging = logging

    def __enter__(self):
        self.connector = self._create_connector(self.logging)
        self.cursor = self.connector.cursor(buffered=True)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connector.commit()
        self.connector.close()
        self.cursor.close()

    def _create_connector(self, logging):
        return mysql.connector.connect(
            host=logging.host,
            user=logging.user,
            password=logging.password,
            database=logging.table
        )


class MysqlHandler:
    def __init__(self, config_file, db_name):
        self.name = db_name
        self.logging = self._read_logging(config_file)

    def fetchone(self, query):
        with Connection(self.logging) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    def fetchmany(self, query, nb):
        with Connection(self.logging) as cursor:
            cursor.execute(query)
            return cursor.fetchmany(nb)

    def fetchall(self, query):
        with Connection(self.logging) as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def insert_value(self, query, values):
        with Connection(self.logging) as cursor:
            if isinstance(values, list):
                cursor.executemany(query, values)
            else:
                cursor.execute(query, values)

    def update_value(self, query):
        with Connection(self.logging) as cursor:
            cursor.execute(query)


    def _read_logging(self, config_file):
        config_parser = ConfigParser()
        config_parser.read(config_file)
        logging = DbAccess()
        logging.host = config_parser.get(self.name, "MYSQL_DATABASE_HOST")
        logging.user = config_parser.get(self.name, "MYSQL_DATABASE_USER")
        logging.password = config_parser.get(self.name, "MYSQL_DATABASE_PASSWORD")
        logging.table = config_parser.get(self.name, "MYSQL_DATABASE_DB")
        logging.validate()
        return logging


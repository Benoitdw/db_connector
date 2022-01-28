import mysql.connector
from configparser import ConfigParser
from db_handler_config import DbAccess

class DbHandler:
    def __init__(self, config_file, db_name):
        self.name = db_name
        self.connector = self._create_connector(config_file)
        print(self.connector)
        self.cursor = self.connector.cursor()

    def _create_connector(self, config_file):
        logging = self._read_logging(config_file)
        return mysql.connector.connect(
            host=logging.host,
            user=logging.user,
            password=logging.password,
            database=logging.table
        )

    def _query(self, query):
        self.cursor.execute(query)

    def fetchone(self, query):
        self._query(query)
        return self.cursor.fetchone()

    def fetch_many(self, query, nb):
        self._query(query)
        return self.cursor.fetchmany(nb)

    def fetch_all(self, query):
        self._query(query)
        return self.cursor.fetchall()

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

    def __del__(self):
        self.connector.close()
        self.cursor.close()


from db_connector import MysqlHandler


class TestMysql:
    logging_file = 'db_access.ini'
    skywalker_handler = MysqlHandler(logging_file, 'SKYWALKER')
    query = "select * from TASK_STATE where analysis_name like '003441'"

    def test_fetch_one(self):
        assert len(self.skywalker_handler.fetchone(self.query)) == 4

    def test_many(self):
        nb = 5
        assert len(self.skywalker_handler.fetchmany(self.query, nb)) == nb
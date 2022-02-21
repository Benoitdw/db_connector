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

    def test_insert_one(self):
        query = "INSERT INTO TASK_STATE (task_id, analysis_name, task_name, task_state) VALUES (%s, %s, %s, %s)"
        values = [('test', '02233', 'test', 'completed')]
        self.skywalker_handler.insert_value(query, values)

    def test_insert_multiple(self):
        query = "INSERT INTO TASK_STATE (task_id, analysis_name, task_name, task_state) VALUES (%s, %s, %s, %s)"
        values = [('test', '02233', 'test', 'completed'),
                  ('test2', '02233', 'test2', 'failed')]
        self.skywalker_handler.insert_value(query, values)

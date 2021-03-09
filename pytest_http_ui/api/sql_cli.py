import pymysql
import aiomysql


class sql_cli:
    def __init__(self, host=None, user='Anyshare', password="asAlqlTkWU0zqfxrLTed", database='domain_mgnt'):
        self.host = host
        self.port = 3320
        self.user = user
        self.password = password
        self.database = database
        # self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
        #                           db=self.database)

    def __enter__(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                  db=self.database)
        return self.db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.cursor().close()


class aiomysql_cli:
    def __init__(self, host=None, user='Anyshare', password="asAlqlTkWU0zqfxrLTed", database='domain_mgnt'):
        self.host = host
        self.port = 3320
        self.user = user
        self.password = password
        self.database = database

    # async def get_cursor(self):
    #     conn = await aiomysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
    #                                   db=self.database)
    #     cur = await conn.cursor()
    #     return cur, conn

    async def __aenter__(self):
        self.conn = await aiomysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                           db=self.database)
        # self.cur = await conn.cursor()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

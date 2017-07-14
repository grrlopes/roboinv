import mysql
import mysql.connector
__author__ = 'Gabriel Lopes 07/06/17'


class Conector:
        def __init__(self):
            self.ip = '192.168.236.104'
            self.bd = 'tpd'
            self.user = ''
            self.senha = ''
            self.conn = None
            self.cursor = None
            self.query = None
            self.param = None

        def tercnx(self):
            self.conn = mysql.connector.connect(user=self.user, password=self.senha, host=self.ip, database=self.bd)
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.query, self.param)

from conector import Conector
import csv
import base64
__author__ = 'Gabriel Lopes 07/06/17'


class Invindral(Conector):
    def __init__(self):
        Conector.__init__(self)
        self.local = '/home/gabriel/PycharmProjects/Invindra/Lista'
        self.separa = ';'
        self.lista = []
        self.loginips = []
        self.loginipsarrei = []
        self.msg = None
        self.direrror = None

    def ler(self):
        try:
            with open(self.local, 'r') as local:
                ler = csv.reader(local, delimiter=self.separa)
                for l in ler:
                    self.lista.append(l)
        except FileNotFoundError:
            print('Arquivo não encontrado')
        except IsADirectoryError:
            print('Dir errado')

    def negrao(self):
        self.ler()
        for ips in self.lista:
            self.query = "select server.host, server.ip, user.user, user.passwd " \
                         "from usuarios user INNER JOIN servidores server ON " \
                         "user.svr = server.id where server.ip = %s" % "'"+ips[0]+"'"
            Conector.tercnx(self)
            for i in self.cursor:
                passw = base64.b64decode(i[3]).decode()
                if i[2] == 'root':
                    valor = i[1]+';'+i[2]+';'+passw
                    self.loginips.append(valor)
            self.cursor.close()
            self.conn.close()
        self.loginipsarrei = csv.reader(self.loginips, delimiter=self.separa)

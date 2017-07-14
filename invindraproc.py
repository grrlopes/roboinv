from invindral import Invindral
from pexpect import pxssh
import paramiko
__author__ = 'Gabriel Lopes 07/06/17'


class Invindraproc(Invindral):
    def __init__(self):
        Invindral.__init__(self)
        self.error = []
        self.eu = []
        self.nossa = None
        self.ssh = None

    def process(self):
        self.negrao()
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )
        for i in self.loginipsarrei:
            try:
                self.ssh.connect(i[0], username=i[1], password=i[2])
            except paramiko.NoValidConnectionsError(errors):
                print('e'1)
            """try:
                stdin, stdout, stderr = self.ssh.exec_command("uname")
                data = stdout.readlines()
                print(data)
            except paramiko.AuthenticationException as f:
                print(f)
            except paramiko.BadHostKeyException as c:
                print(c)
            #ssh.close()"""

    def process111(self):
        self.negrao()
        for i in self.loginipsarrei:
            try:
                s = pxssh.pxssh()
                s.login(i[0], i[1], i[2])
                s.sendline('uname')
                s.prompt()

                """s.sendline('hostname; cat /etc/issue; free -m |egrep --color=never -i mem; '
                           'cat /proc/cpuinfo |egrep --color=never -i processor; '
                           'fdisk -l |egrep --color=neve -i Disk; iostat -eE; ps -ef')
                s.prompt()
                teste = s.before.decode()
                print(teste)"""
                s.logout()
            except pxssh.ExceptionPexpect as e:
                self.error.append('Com problema '+i[0])
        for i in self.error:
            print(i)

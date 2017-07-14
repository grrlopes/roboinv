#!/usr/bin/env python3
from invindraproc import Invindraproc
__author__ = 'Gabriel Lopes 07/06/17'


class Executa(Invindraproc):
    def __init__(self):
        Invindraproc.__init__(self)
        self.process()


class Principal:
    if __name__ == "__main__":
        Executa()


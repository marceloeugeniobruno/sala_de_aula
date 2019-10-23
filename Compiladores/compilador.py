from collections import deque
from enum import Enum


class Token:

    def __init__(self, tipo, lexema, linha, coluna):
        self.tipo = tipo
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna

    @property
    def __str__(self):
        return f'Tipo -> {self.tipo} Lexema -> {self.lexema} Linha -> {self.linha} Coluna -> {self.coluna}'


def abre_arquivo(arq):
    arquivo = open(arq)
    li = deque(arquivo.read())
    return li


def char_aceitos(ch):
    listchar = '0123456789_abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ().+-*=;: '
    if ch in listchar:
        return True
    elif ch == '\n' or ch == '\t':
        return True
    return False


class Tipo(Enum):

    SPROGRAMA = 'programa'
    SVAR = 'var'
    SINICIO = 'inicio'
    SFIM = 'fim'
    SATRIBUICAO = ':='
    STIPO = ':'
    SESCREVA = 'escreva'
    SINTEIRO = 'inteiro'
    SPONTO_E_VIRGULA = ';'
    SPONTO = '.'
    SMAIS = '+'
    SMENOS = '-'
    SMULTIPLICACAO = '*'
    SNUMERO = 'numero'
    SIDENTIFICADOR = 'identificador'
    SABRE_PARENTESIS = '('
    SFECHA_PARENTESIS = ')'
    SERRO = 'erro'

"""
Programa 2  9
inicio   10 15
var      16 18
escreva  19 25
fim      26 28
:=       29 30
"""


class Lexico:

    def __init__(self, arquivo):
        self.estado = 0
        self.lista_char = abre_arquivo(arquivo)
        self.lista = []

    def analisa(self):
        for i in self.lista_char:
            if char_aceitos(i):
                self.estado = 99
            if self.estado == 0:
                if i.isnumeric():
                    self.estado = 1
                elif i == 'p':
                    self.estado = 2
                elif i == 'i':
                    self.estado = 10
                elif i == 'v':
                    self.estado = 16
                elif i == 'e':
                    self.estado = 19
                elif i == 'f':
                    self.estado = 26
                elif i == ':':
                    self.estado = 29


class TS:

    def __init__(self):
        self.mapa = {}

    def inser_t (self):
        return 1

    def looku_p(self):
        return 1

    def set_atributo(self , chave, atributo, valor):
        return 1

    def get_atributo(self, chave, valor):
        return 1


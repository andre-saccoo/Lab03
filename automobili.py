import csv
from enum import nonmember

class Automobile:
    def __init__(self,id, marca, modello, anno, numPosti):
        self._id = id
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._numPosti = numPosti

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modello(self):
        return self._modello
    @modello.setter
    def modello(self, value):
        self._modello = value

    @property
    def anno(self):
        return self._anno
    @anno.setter
    def anno(self, value):
        self._anno = value

    @property
    def numPosti(self):
        return self._numPosti
    @numPosti.setter
    def numPosti(self, value):
        self._numPosti = value

    def __str__(self):
        return f'identificatore macchina:{self.id},marca:{self.marca}, modello:{self.modello},anno: {self.anno},numero posti{self.numPosti}'
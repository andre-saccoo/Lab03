import csv
from enum import nonmember

class Automobile:
    def __init__(self,id, marca, modello, anno, numPosti):
        self.id = id
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.numPosti = numPosti

    infile=open(filepath)
    reader = csv.reader(infile)



    def __str__(self):
        return f'identificatore macchina:{self.id},marca:{self.marca}, modello:{self.modello},anno: {self.anno},numero posti{self.numPosti}'




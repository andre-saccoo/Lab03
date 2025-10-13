# definisco la classe Automobile
class Automobile:
    def __init__(self,id, marca, modello, anno, numPosti):
        # gli attributi della classe vengono definiti come privati, la gestione è poi
        # affidata ai metodi dei setter e getter, mantenendo il codice stabile
        self._id = id
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._numPosti = numPosti
        self._disponibile = True

    #definisco i metodi di getter e setter per poter utilizzare e settare gli attributi
    # come se fossero pubblici
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

    # per gestire i noleggi definisco tra gli attributi anche l'attributo booleano
    # disponibile
    @property
    def disponibile(self):
        return self._disponibile
    @disponibile.setter
    def disponibile(self, valore):
        self._disponibile = bool(valore)

    #funzione per stampare la classe formattata
    def __str__(self):
        return f'identificatore macchina: {self.id}, marca: {self.marca}, modello: {self.modello}, anno: {self.anno}, numero posti: {self.numPosti}'
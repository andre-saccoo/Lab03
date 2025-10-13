from automobili import Automobile
import csv

#creo la classe autonoleggio, possiede un nome della società e il nome del responsabile
class Autonoleggio:
    def __init__(self, nome, responsabile):

        self._nome = nome
        self._responsabile = responsabile
        self.listaAutomobili = []

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile
    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def carica_file_automobili(self, file_path):
        try:
            infile = open(file_path, "r", encoding="utf-8")
            reader = csv.reader(infile)
            for riga in reader:
                id, marca, modello, anno, numPosti = riga
                try:
                    anno = int(anno)
                    numPosti = int(numPosti)
                except ValueError:
                    print(f"errore nella scrittura del file")
                    continue
                automobile = Automobile(id, marca, modello, anno, numPosti)
                self.listaAutomobili.append(automobile)
                print(automobile)
            infile.close()
            return self.listaAutomobili
        except FileNotFoundError:
            print("File non trovato")
            return None

    #passo i parametri dal main
    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        id=f"A{len(self.listaAutomobili)+1}"
        automobile = Automobile(id, marca, modello, anno, num_posti)
        self.listaAutomobili.append(automobile)
        return automobile


    def ordina(self, automobile):
        return automobile.marca
    def automobili_ordinate(self):
        listaAutomobiliOrdinata=sorted(self.listaAutomobili, key=self.ordina)
        return listaAutomobiliOrdinata

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO

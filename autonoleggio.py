from automobili import Automobile
import csv

#creo la classe autonoleggio, possiede un nome della società e il nome del responsabile
class Autonoleggio:
    def __init__(self, nome, responsabile,listaAutomobili):

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


    def aggiungi_automobile(self, marca, modello, anno, num_posti, ):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        id=f"A+{len(self.listaAutomobili)+1}"
        marca=input("inserire la marca dell'automobile: ")
        modello=input("inserire la modello dell'automobile: ")
        try:
            anno=input("inserire la anno dell'automobile: ")
        except ValueError:
            print("inserire la anno dell'automobile:")
        try:
            num_posti=int(input("inserire la numero posti: "))
        except ValueError:
            print("inserire la numero posti:")




    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO

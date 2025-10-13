import csv
from enum import nonmember

from automobili import Automobile
from noleggio import Noleggio

#creo la classe autonoleggio, possiede un nome della società e il nome del responsabile
class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self.listaAutomobili = []
        self.listaNoleggio = []
        self.codiceNoleggio = 0

    # per gli attributi della classe definisco i metodi setter e getter per utilizzare gli
    # attributi definiti privati come se fossero pubblici
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

    #prende la lista delle macchine restituisce solo la marca e ordina per attributo marca
    def ordina(self, automobile):
        return automobile.marca
    def automobili_ordinate(self):
        return sorted(self.listaAutomobili, key=self.ordina)

    # definisco la funzione che gestisce i nuovi noleggi, inseriti in una lista di oggetti noleggio definita sopra
    # la funzione controlla che la moto sia noleggiabile, se è disponibile dopo averla presa la rende non disponibile
    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        trovato=False
        automobile=None

        #scorro i codici delle auto e li confronto se la trovo esco dal ciclo
        #perchè l'auto è presente nel sistema
        for a in self.listaAutomobili:
            if a.id == id_automobile:
                trovato=True
                automobile=a
                break

        #se non trova l'automobile lo segnala
        if  not trovato:
            raise Exception(f"Automobile {id_automobile} non presente nel sistema! ")

        # se l'automobile è presente ma già noleggiata
        if not automobile.disponibile:
            raise ValueError(f" Automobile {id_automobile} già noleggiata! ")

        #se i controlli sono superati
        self.codiceNoleggio += 1
        codice = f"N{self.codiceNoleggio}"
        noleggio=Noleggio(data, id_automobile, cognome_cliente, codice)
        self.listaNoleggio.append(noleggio)

        # rendo la macchina noleggiata, nel tentativo successivo se
        # non termino il noleggio la macchina sarà prenotata
        automobile.disponibile=False

        #restituisco il nuovo noleggio
        return noleggio

# creo la funzione che termina il noleggio e rende di nuovo disponibile la macchina per altri noleggi
    def termina_noleggio(self, id_noleggio):
        noleggioTrovato = None
        for n in self.listaNoleggio:
            if n.CodiceNoleggio == id_noleggio:
                noleggioTrovato = n
                break
        if noleggioTrovato is not None:
            raise ValueError(f"Nessun noleggio trovato con codice '{id_noleggio}'.")
        self.automobile.disponibile=True
        self.listaNoleggio.remove(noleggioTrovato)
        print(f"il noleggio {id_noleggio} è terminato, l'automobile è nuovamente disponibile")
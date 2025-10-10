from automobili import Automobile

class Autonoleggio:
    def __init__(self, nome, responsabile,listaAutomobili):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._responsabile = responsabile
        self.listaAutomobili = []

    def carica_file_automobili(self, file_path):
        try:
            infile=open(file_path, 'r')
            for line in infile:
                a=Automobile(line[0],line[1],line[2],line[3],line[4])
                self.listaAutomobili.append(a)
            infile.close()
        except FileNotFoundError:
            print("file non trovato")
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

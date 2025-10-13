class Noleggio():
    # creo la classe noleggio, possiede un codice noleggio, una data d'inizio
    # un codice automobile prenotata nel noleggio e il cognome della persona che prenota
    def __init__(self, dataInizio, codiceAutomobile, cognome , codiceNoleggio):
        self._codiceNoleggio=codiceNoleggio
        self._dataInizio=dataInizio
        self._codiceAutomobile=codiceAutomobile
        self._cognome=cognome

    # per gli attributi della classe definisco i metodi setter e getter per utilizzare gli
    # attributi definiti privati come se fossero pubblici
    @property
    def CodiceNoleggio(self):
        return self._codiceNoleggio
    @CodiceNoleggio.setter
    def CodiceNoleggio(self,codiceNoleggio):
        self._codiceNoleggio=codiceNoleggio

    @property
    def dataInizio(self):
        return self._dataInizio
    @dataInizio.setter
    def dataInizio(self,dataInizio):
        self._dataInizio=dataInizio

    @property
    def codiceAutomobile(self):
        return self._codiceAutomobile
    @codiceAutomobile.setter
    def codiceAutomobile(self,codiceAutomobile):
        self._codiceAutomobile=codiceAutomobile

    @property
    def cognome(self):
        return self._cognome
    @cognome.setter
    def cognome(self,cognome):
        self._cognome=cognome

    # definisco la classe __str__ per stampare in modo formattato la classe
    def __str__(self):
        return (f"Noleggio {self._codiceNoleggio}: "
                f"data inizio = {self._dataInizio}, "
                f"auto = {self._codiceAutomobile}, "
                f"cliente = {self._cognome}")

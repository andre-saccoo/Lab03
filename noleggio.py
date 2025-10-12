class Noleggio():
    def __init__(self, codiceNoleggio, dataInizio, codiceAutomobile, cognome):
        self._codiceNoleggio=codiceNoleggio
        self._dataInizio=dataInizio
        self._codiceAutomobile=codiceAutomobile
        self._cognome=cognome
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

    def __str__(self):
        return (f"Noleggio {self._codiceNoleggio}: "
                f"data inizio = {self._dataInizio}, "
                f"auto = {self._codiceAutomobile}, "
                f"cliente = {self._cognome}")

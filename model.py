import random

# ---> MODEL, LOGICA PURA DELL'ESERCIZIO

class Model(object):
    # vado a implementare tutta la logica del mio programma
    # mi serve sapere numero massimo, tentativi rimanenti, e tentativi max
    # gli fornisco tutto io
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6
        self._T = self._Tmax
        self._segreto = None

    # questo metodo resetta lo stato del gioco.
    # imposta il segreto a un valore randomico fra 0 e Nmax
    # e ripristina il numero di tentativi rimanenti
    def reset(self):
        self._segreto = random.randint(0, self._Nmax)
        self._T = self._Tmax
        print(self._segreto)

    def play(self, tentativo):
        # questo metodo riceve come argomento un valore intero,
        # che sarà il tentativo del giocatore, e lo confronta con il segreto

        # -1 se il segreto è più piccolo del tentativo
        # 0 se il segreto è uguale del tentativo
        # 1 se il segreto è più grande del tentativo
        # 2 se non ho più tentativi disponibili

        self._T -= 1 # decremento vite ( ogni tentativo consuma una vita )

        if tentativo == self._segreto:
            # ho vinto
            return 0

        if self._T == 0:
            # allora non ho più vite perciò non posso più giocare
            return 2

        elif tentativo > self._segreto:
            # il segreto è più piccolo del tentativo
            return -1
        else:
            # il segreto è più grande del tentativo
            return 1

    # queste 4 property mi permettono un accesso controllato ( lettura e non modifica)

    @property
    def Nmax(self): # accedo alla variabile Nmax attraverso la property
        return self._Nmax

    @property
    def Tmax(self):  # accedo alla variabile Tmax attraverso la property
        return self._Tmax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto


if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(40))
    print(m.play(70))
    print(m.play(50))
    print(m.play(60))
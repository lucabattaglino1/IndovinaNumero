from view import View
from model import Model
import flet as ft

# ---> CONTROLLER, IL CERVELLO, IL MEDIATORE TRA VIEW E MODEL

class Controller(object):
    # qui ci sono i riferimenti alla view e l'istanza del model
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    # chiedo al modello qual'è l'Nmax e lo restituisco --> per servire la view
    def getNmax(self):
        return self._model.Nmax

    # chiedo al modello qual'è il Tmax e lo restituisco --> per servire la view
    def getTmax(self):
        return self._model.Tmax

    # cosa succede quando premo il bottone NUOVA PARTITA ?
    def reset(self, e):
        self._model.reset() # resetto lo stato del gioco lato modello
        self._view._txtT.value = self._model.T # vado a resettare il valore di tentativi chiedendolo al modello
        self._view._lvOut.controls.clear() # pulisco le stringhe
        self._view._lvOut.controls.append(ft.Text("Inizia il gioco! Indovina a quale numero sto pensando")) # messaggio iniziale

        self._view.update() # per aggiornare la pagina

    # cosa succede quando premo il bottone INDOVINA ?
    def play(self, e):
        tentativoStr = self._view._txtInTentativo.value # leggo l'imput dell'utente

        # gestisco un eccezione perchè l'utente può scrivermi qualsiasi carattere
        # se la versione fallisce scrivo l'errore con un print e esco
        # se supero il controllo posso giocare
        try:
            tentativo = int(tentativoStr) # controllo che sia un intero
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore, devi inserire un valore numerico"))
            self._view.update()
            return

        risultato = self._model.play(tentativo) # qui avviene la logica, se passato il controllo

        # in questi 4 casi vado a gestire i risultati
        # li appendo poi alla ListView all'interno della View
        if risultato == 0:
            # ho vinto, aggiorno l'interfaccia grafica di conseguenza
            self._view._lvOut.controls.append(ft.Text(f"Hai vinto, il valore corretto era: {tentativo}", color = "green"))
            self._view.update()
            return

        elif risultato == 2:
            # non ho più vite, aggiorno l'interfaccia grafica di conseguenza
            self._view._lvOut.controls.append(ft.Text(f"Hai perso, il valore corretto era {self._model.segreto}"))
            self._view.update()
            return

        elif risultato == -1:
            # il segreto è più piccolo del tentativo, aggiorno l'interfaccia grafica di conseguenza
            self._view._lvOut.controls.append(ft.Text(f"Ritenta, il segreto è più piccolo di {tentativo}"))
            self._view.update()
            return

        else:
            # il segreto è più grande del tentativo, aggiorno l'interfaccia grafica di conseguenza
            self._view._lvOut.controls.append(ft.Text(f"Ritenta, il segreto è più grande di {tentativo}"))
            self._view.update()
            return
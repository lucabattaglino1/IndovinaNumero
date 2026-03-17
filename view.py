import flet as ft

# ---> INTERFACCIA GRAFICA

class View(object):
    # imposto la finestra e preparo il collegamento al controller
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2026 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        # metodo per scrivere tutte le definizioni per pulsanti, caselle di testo...
        self._titolo = ft.Text("Indovina il numero", color="blue", size=24) # imposto titolo

        # la view non sa niente, perciò chiedo al controller l'Nmax, il Tmax e i tentativi rimanenti
        # il controller avrà dei metodi per prenderli dal model
        self._txtNmax = ft.TextField(label = "Numero Max",
                                     value = self._controller.getNmax(),
                                     disabled = True)

        self._txtTmax = ft.TextField(label="Numero Tentativi Max",
                                     value=self._controller.getTmax(),
                                     disabled=True)

        self._txtT = ft.TextField(label="Tentativi Rimanenti",
                                    disabled=True)

        # li inserisco in una riga
        self._row1 = ft.Row(controls = [self._txtNmax, self._txtTmax, self._txtT])

        # qui ho il valore che andrà l'utente a scrivere
        self._txtInTentativo = ft.TextField(label="valore")

        # qui ho i miei due bottoni dove vado a chiamare il controller per avere un'azione
        self_btnReset = ft.ElevatedButton(text = "Nuova partita", on_click = self._controller.reset)
        self_btnPlay = ft.ElevatedButton(text = "Indovina", on_click = self._controller.play)

        self._row2 = ft.Row(controls = [self._txtInTentativo, self_btnReset, self_btnPlay])

        # per stampare la cronologia del gioco
        self._lvOut = ft.ListView(expand = True)

        # li inserisco tutti nella pagina
        self._page.add(self._row1, self._row2, self._lvOut)
        self._page.update()

    def setController(self,controller):
        # per far conoscere view e controller, qualsiasi cosa succeda chiamo il controller
        self._controller = controller

    # serve per aggiornare la pagina dopo le modifiche
    def update(self):
        self._page.update()
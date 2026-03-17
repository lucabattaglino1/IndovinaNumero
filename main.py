import flet as ft
from controller import Controller
from view import View

# creo la pagina, creo la view, creo il controller, collego view e controller
def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.setController(c) # la view deve sapere chi chiamare quando premi i bottoni
    v.caricaInterfaccia() # carico l'interfaccia

ft.app(target=main)
import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        year = int(self._view._txtAnno.value)
        if not self._model.valid_year(year):
            print("Anno non valido")
            return
        self._view._dd_stato.options.clear()
        self.populate_dd_stato()
        self._model.buildGraph(year)
        self._model.printGraphDegree()
        return

    def stato_selezionato(self, e):
        stato = self._view._dd_stato.value
        self._view._btnStatiRaggiungibili.disabled = False
        self._view.update_page()

    def populate_dd_stato(self):
        stati = self._model.get_stati()
        for stato in stati:
            self._view._dd_stato.options.append(ft.dropdown.Option(key=stato.ccode, text=stato.stateName))

    def handleStatiRaggiungibili(self, e):
        self._model.statiRaggiungibili(self._view._dd_stato.value)
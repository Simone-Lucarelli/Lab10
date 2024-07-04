import time

import networkx as nx

from database.DAO import DAO

def timer(func):
    def wrapper(funct):
        start_time = time.time()
        funct()
        return time.time() - start_time
    return wrapper()


class Model:

    def __init__(self):
        self.graph: nx.Graph = None
        self.countries = []
        self.id_Map = {}
        self.listaStati = []

    def printBorders(self, year):
        borders = DAO.getBorders(year)
        for b in borders:
            print(b)

    def loadCountries(self):
        self.countries = DAO.getCountries()
        for country in self.countries:
            self.id_Map[country.ccode] = country
    def buildGraph(self, year):
        self.graph = nx.Graph()
        self.loadCountries()
        print(self.countries)
        self.graph.add_nodes_from(self.countries)
        borders = DAO.getBorders(year)
        for border in borders:
            self.graph.add_edge(self.id_Map[border.state1no], self.id_Map[border.state2no])

    def printGraphDegree(self):
        self.connectedComponents()
        sorted_countries = sorted(self.graph.nodes, key=lambda x: x.stateName)
        for country in sorted_countries:
            num_borders = self.graph.degree(country)
            print(f"{country.stateName} -- {num_borders} vicini")

    def connectedComponents(self):
        print(f"Il grafo ha {nx.number_connected_components(self.graph)} componenti connesse")

    def get_stati(self):
        self.loadCountries()
        return self.countries

    def valid_year(self, year):
        if year > 1815 and year < 2017:
            return True
        return False

    def statiRaggiungibili(self, stato_id):
        self.listaStati.clear()
        stato = self.id_Map[int(stato_id)]
        statiRaggiungibili = [stato]
        self.ricorsione(stato, statiRaggiungibili)
        self.listaStati.sort()
        lista1 = self.listaStati
        print(f"Stati raggiungibili: {lista1}")
        lista2 = []
        for s in nx.bfs_successors(self.graph, stato):
            for e in s[1]:
                if e not in lista2:
                    lista2.append(e)
        lista2.sort()
        print(f"Stati raggiungibili BFS: {lista2}")
        lista3 = []
        for s in nx.dfs_successors(self.graph, stato):
            for e in s[1]:
                if e not in lista3:
                    lista3.append(e)
        print(list(set(lista3) - set(lista2)))


    def ricorsione(self, stato, statiRaggiungibili):
        neighbors = self.graph[stato]
        da_aggiungere = []
        for s in neighbors:
            if s not in statiRaggiungibili:
                da_aggiungere.append(s)
        if len(da_aggiungere) == 0:
            self.copia(statiRaggiungibili)
            return
        else:
            for s in da_aggiungere:
                statiRaggiungibili.append(s)
                self.ricorsione(s, statiRaggiungibili)

    def copia(self, stati):
        for stato in stati:
            if stato not in self.listaStati:
                self.listaStati.append(stato)

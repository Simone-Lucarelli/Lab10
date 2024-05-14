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
        for node in self.graph.nodes:
            print (f"{node} {self.graph.degree(node)}")
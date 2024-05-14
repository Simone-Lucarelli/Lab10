from model.model import Model
import networkx as nx

my_model = Model()
my_model.printBorders(1999)
my_model.buildGraph(1999)
my_model.printGraphDegree()
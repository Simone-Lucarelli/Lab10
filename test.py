from model.model import Model
import networkx as nx

my_model = Model()
my_model.buildGraph(2000)
my_model.printGraphDegree()
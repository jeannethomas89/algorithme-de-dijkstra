from time import sleep
from Affichage import Affichage
from Dijkstra import Dijkstra
import random
import numpy
import plotly
from Graphe import Graphe
from Vertice import Vertice

plotly.io.renderers.default = "browser"
print("Entrez le nombre de sommets du graphe")
n = int(input())
graphe = Graphe()
for i in range(n):
    pointI = Vertice(str(i),
                     "rgb({},{},{})".format(120, 12, 255))
    graphe.add_vertice(pointI)
for i in range(n):
    a = int(numpy.random.normal(1 + n / 5, 0.5))  # nbr de chemins crées pour chaque pt du graphe:
    a = max(1, min(a, n))
    for j in range(1, a + 1):
        poids = int(random.randint(1, 100))  # j'ai rajouté ca pour tester le programme
        pointB = graphe.get_vertices()[i]
        pointI = graphe.get_vertices()[i]
        while pointI.__eq__(pointB):
            b = int(random.randint(0, n - 1))
            pointB = graphe.get_vertices()[b]
        graphe.add_edge(pointI, pointB, poids)
graphe.setAllPosition()
for vertice in graphe.get_vertices():
    print(vertice.get_nom() + " : " + str(vertice.get_neighbours()))
    for neighbour in vertice.get_neighbours():
        print(vertice.get_nom() + " - " + str(neighbour.get_nom()) + " :" + str(graphe.get_edge(vertice, neighbour).getWeight()))

view = Affichage()
view.trace(graphe)
dij = Dijkstra(graphe)
result = dij.start(graphe.get_vertices()[0], graphe.get_vertices()[n - 1])
colors = {}
print(result)
for vertice in graphe.get_vertices():
    colors[vertice] = (vertice.get_color())

for point in result:
    sleep(2)
    colors[point] = "rgb(255,0,0)"
    tab = []
    for color in colors.values(): # convertir le dictvalue en liste
        tab.append(color)
    view.update_fig_color(tab)

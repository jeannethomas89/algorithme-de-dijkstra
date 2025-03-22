from Vertice import Vertice
from Graphe import Graphe


class Dijkstra():
    # initialisation de l'algo
    def __init__(self, graphe: Graphe):
        self.graphe = graphe
        self.distance = {}
        self.predecesseur = {}
        for vertice in self.graphe.get_vertices():
            self.distance[vertice.nom] = float('inf')

    # Recherche d'un sommet de distance minimale
    def __distance_min(self, Q: list) -> Vertice:
        min = float('inf')
        vertice_min = None
        for vertice in Q:
            if self.distance[vertice.nom] < min:
                min = self.distance[vertice.nom]
                vertice_min = vertice
        return vertice_min

    # Mise à jour des distances
    def __maj_distances(self, v1: Vertice, v2: Vertice):
        poids = self.distance[v1.nom] + self.graphe.get_edge(v1, v2).getWeight()
        if self.distance[v2.nom] > self.distance[v1.nom] + poids:
            self.distance[v2.nom] = self.distance[v1.nom] + poids
            self.predecesseur[v2.nom] = v1

    def start(self, first_vertice: Vertice, end_vertice: Vertice) -> list:
        self.distance[first_vertice.nom] = 0
        Q = self.graphe.get_vertices().copy()
        while Q:  # tant que Q n'est pas vide
            v1 = self.__distance_min(Q)
            if v1 in Q:
                Q.remove(v1)
            else:
                break
            for v in self.graphe.get_neighbours(v1):

                if self.graphe.get_neighbours(v1):
                    self.__maj_distances(v1, v)
        chemin = []
        v = end_vertice
        while not v.__eq__(first_vertice):
            if v.nom == end_vertice.nom:
                chemin.append(end_vertice)
            else:
                chemin.append(v)
            v = self.predecesseur[v.get_nom()]
        chemin.append(first_vertice)
        chemin.reverse()
        return chemin

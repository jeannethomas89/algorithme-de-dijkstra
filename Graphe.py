import math
import random
from Vertice import Vertice
from Edge import Edge


class Graphe():
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    # changement des listes en dictionnaires
    def add_vertice(self, vertice: Vertice) -> None:
        if vertice.nom not in self.vertices.keys() and vertice.position not in self.vertices.keys():
            self.vertices[vertice.get_nom()] = vertice  # ajout du point au dico
            # verif de pas avoir des doublons de coordonnées

    def get_vertices(self) -> list:
        return list(self.vertices.values())

    def add_edge(self, a: Vertice, b: Vertice, poids: float) -> None:

        if not self.edge_existence(a, b):
            self.add_vertice(a)
            self.add_vertice(b)
            a.add_neighbour(b)
            edge = Edge(a, b, "0000", poids)
            self.edges[(a, b)] = edge  # ajout du chemin au dico en lui passant un couple de points en clé

    def edge_existence(self, a: Vertice, b: Vertice) -> bool:
        if (a, b) in self.edges.keys():
            return True
        else:
            return False

    # renvoie le chemin entre a et b stocké dans le dico
    def get_edge(self, a: Vertice, b: Vertice):
        if not self.edge_existence(a, b):
            return None
        return self.edges[(a, b)]

    def get_neighbours(self, a: Vertice) -> set:
        if a in self.vertices.values():
            return a.get_neighbours()
        else:
            return set()

    def get_edges(self) -> list:
        return list(self.edges.values())

    def setAllPosition(self):
        for i in range(20):
            kCoumlomb = 0.00000000000000000001
            for mainVertice in self.vertices.values():
                for otherPoint in self.vertices.values():
                    if not otherPoint.__eq__(mainVertice):
                        if mainVertice.getDistance(otherPoint.getPosition()) == 0:
                            anglededep = random.randint(0, 360)
                            directionalVector = (math.cos(anglededep) - math.sin(anglededep),
                                                 math.sin(anglededep) + math.cos(anglededep))
                            mainVertice.set_position((mainVertice.getPosition()[0] + directionalVector[0] * 5,
                                                      mainVertice.getPosition()[1] + directionalVector[1] * 5))
                        else:
                            dist = mainVertice.getDistance(otherPoint.getPosition())
                            unitedVector = mainVertice.getUnitedVector(otherPoint)
                            force = kCoumlomb / dist
                            mainVertice.set_position((mainVertice.getPosition()[0] + force * unitedVector[0],
                                                      mainVertice.getPosition()[1] + force * unitedVector[1]))
            for mainVertice in self.vertices.values():
                mainVertice.setPositionWithHookForce()

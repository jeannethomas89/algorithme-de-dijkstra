import math
class Vertice:

    def __init__(self, nom: str, color: str = "#888", position=(1, 1)):
        self.nom = nom
        self.color = color
        self.neighbours = set()
        self.position = position

    def getPosition(self) -> tuple:
        return self.position

    def get_nom(self) -> str:
        return self.nom

    def get_color(self) -> str:
        return self.color

    def get_neighbours(self) -> set:
        return self.neighbours

    def set_nom(self, nom: str) -> None:
        self.nom = nom

    def set_color(self, color: str) -> None:
        self.color = color

    def set_neighbours(self, neighbours: set) -> None:
        self.neighbours = neighbours

    def set_position(self, position: tuple) -> None:
        self.position = position

    def add_neighbour(self, point) -> None:
        self.neighbours.add(point)

    def add_neighbours(self, voisins: set) -> None:
        self.neighbours.union(voisins)

    def getDistance(self, point: tuple) -> float:
        return math.sqrt((point[0] - self.position[0]) ** 2 + (point[1] - self.position[1]) ** 2)

    def __normalize(self, vector: tuple) -> tuple:
        if abs(self.getDistance(vector)) < 10E-6:
            return vector[0] / self.getDistance(vector), vector[1] / self.getDistance(vector)
        else:
            return vector

    def getUnitedVector(self, point: tuple) -> tuple:
        AB = (-point.getPosition()[0] + self.position[0], -point.getPosition()[1] + self.position[1])
        return self.__normalize(AB)

    def setPositionWithHookForce(self) -> None:
        k = 0.002
        Lideale = 5
        for point in self.get_neighbours():
            AB = (-point.getPosition()[0] + self.position[0], -point.getPosition()[1] + self.position[1])
            unitaryVector = self.__normalize(AB)
            normForce = k * (Lideale - self.getDistance(AB))
            self.set_position(
                (unitaryVector[0] * normForce + self.position[0], unitaryVector[1] * normForce + self.position[1]))

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.nom == other.nom

    def __hash__(self) -> int:
        return hash(self.nom)

    def __repr__(self) -> str:
        return self.nom

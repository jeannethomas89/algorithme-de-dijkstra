from Vertice import Vertice

class Edge:
    def __init__(self, a: Vertice, b: Vertice, color: str = 'r', weight: float = 0):
        self.chemin = (a, b)
        self.color = color
        self.weight = weight

    def getChemin(self):
        return self.chemin

    #ajout fonction qui renvoit l'origine du chemin
    def get_origine(self):
        return self.chemin[0]

    def get_end(self):
        return self.chemin[1]

    def getColor(self) -> str:
        return self.color

    def getWeight(self) -> float:
        return self.weight

    def setColor(self, color: str) -> None:
        self.color = color

    def setWeight(self, weight: float) -> None:
        self.weight = weight
    def getPosOrigine(self):
        return self.chemin[0].getPosition()
    def getPosEnd(self):
        return self.chemin[1].getPosition()

    def __eq__(self, other) -> bool:
        if other is None :
            return False
        return self.chemin[0].__eq__(other.chemin[0]) and self.chemin[1].__eq__(other.chemin[1])

    def __hash__(self) -> int:
        return hash((self.chemin[0], self.chemin[1]))

    def __repr__(self) -> str:
        return f"Edge({self.chemin[0]}, {self.chemin[1]})"


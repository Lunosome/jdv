import pyxel

class Grille:
    
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.cellules = [[0] * largeur for _ in range(hauteur)]

    def voisines(self, x, y):
        voisines = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                voisin_x, voisin_y = x + i, y + j
                if 0 <= voisin_x < self.largeur and 0 <= voisin_y < self.hauteur and (i != 0 or j != 0):
                    voisines.append(self.cellules[voisin_y][voisin_x])
        return voisines

    def tour(self):
        pass

    def remplir(self):
        pass

    def afficher(self):
        pass

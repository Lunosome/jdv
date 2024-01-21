import pyxel
from grille import Grille, Cellule

CASE = 6

class Interface:

    def __init__(self):
        self.grille = Grille(128 // CASE, 128 // CASE)  # Crée une instance de Grille
        pyxel.init(128, 128, title="Jeu de la vie")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.grille.tour()  # Utilise la méthode tour de l'instance de Grille

    def draw(self):
        pyxel.cls(0)
        for x in range(self.grille.largeur):
            for y in range(self.grille.hauteur):
                if self.grille.get_cellule(x, y).viv:
                    pyxel.rect(x * CASE, y * CASE, CASE, CASE, 7)

Interface()

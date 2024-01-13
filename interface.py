import pyxel
from grille import Grille, Cellule

CASE = 6
class interface:

    def __init__(self):
        pyxel.init(128,128, title="Jeu de la vie")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        Grille.tour()
    

    def draw(self):
        def draw(self):
        pyxel.cls(0)
        for x in range(Grille.c.x):
            for y in range(Grille.c.y):
                if Grille.c[x][y].vivante:
                    pyxel.rect(x * CASE, y * CASE, CASE, CASE, 7)



interface()

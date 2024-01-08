from grille import Grille, Cellule

g = Grille(3,4)

c = g.get_cellule(2,1)
c.calcule_etat_futur()
assert c.vivra == False
c.viv = True
c.calcule_etat_futur()
assert c.vivra == False
class Cellule:
    def __init__(self, coordonnee_x : int, coordonnee_y : int, grille : Grille):
        self.viv = False
        self.vivra = False
        self.x = coordonnee_x
        self.y = coordonnee_y
        self.g = grille
    
    def nb_viv(self):
        pass

    def calcule_etat_futur(self):
        """détermine état à venir de la cellule au prochain tour"""
        pt = self.g.voisines(self.x, self.y)
        if self.viv == True and (pt == 2 or pt == 3):
            self.vivra = True
        elif self.viv == False and self.g.voisines(self.x, self.y) == 3:
            self.vivra = True
        else :
            self.vivra = False

    def Maj(self):
        """met à jour la cellule en affectant l'état à venir vivra à l'attribut actuel vivante"""
        self.viv = self.vivra

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
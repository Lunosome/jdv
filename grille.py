###############################################        
### Class Cellule
###############################################

class Cellule:
    def __init__(self, coordonnee_x: int, coordonnee_y: int, grille):
        self.viv = False
        self.vivra = False
        self.x = coordonnee_x
        self.y = coordonnee_y
        self.g = grille

    def nb_viv(self):
        """renvoie un entier qui est le nombre de voisines vivantes"""
        voisines = self.g.voisines(self.x, self.y)
        nb = 0  # initialise nb à 0
        for _ in voisines:
            nb += 1
        return nb

    def calcule_etat_futur(self):
        """détermine l'état à venir de la cellule au prochain tour"""
        n = self.nb_viv()
        if self.viv and (n == 2 or n == 3):
            self.vivra = True
        elif not self.viv and n == 3:
            self.vivra = True
        else:
            self.vivra = False

    def Maj(self):
        """met à jour la cellule en affectant l'état à venir (vivra) à l'attribut actuel (vivante)"""
        self.viv = self.vivra


###############################################        
### Class Grille
###############################################

class Grille:
    
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.c = [[Cellule(x, y, self) for x in range(largeur)] for y in range(hauteur)]

    def voisines(self, x, y):
        # va mettre dans le tableau voisines les cellules qui sont vivantes autour de la cellule donnée
        voisines = []
        for i in range(max(x - 1, 0), min(x + 1, self.largeur)):
            for j in range(max(y - 1, 0), min(y + 1, self.hauteur)):
                if not (i == x and j == y):  # exclut la cellule elle-même
                    voisines.append(self.get_cellule(i, j))
        return voisines

    def get_cellule(self, x, y):
        return self.c[y][x]

    def tour(self):
        for x in range(self.largeur):
            for y in range(self.hauteur):
                self.c[y][x].calcule_etat_futur()
        for x in range(self.largeur):
            for y in range(self.hauteur):
                self.c[y][x].Maj()

    def remplir(self):
        for x in range(self.largeur):
            for y in range(self.hauteur):
                self.c[y][x].viv = True

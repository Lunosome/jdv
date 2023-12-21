class Cellule:
    def __init__(self, coordonnee_x : int, coordonnee_y : int, grille : Grille):
        self.viv = False
        self.vivra = False
        self.x = coordonnee_x
        self.y = coordonnee_y
        self.g = grille

    def calcule_etat_futur(self):
        """détermine état à venir de la cellule au prochain tour"""

    def Maj(self):
        """met à jour la cellule en affectant l'état à venir vivra à l'attribut actuel vivante"""
        self.vivante = self.vivra

class Grille:
    
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.c = [[Cellule(x, y, self) for x in hauteur ]for y in largeur]

    def voisines(self, x, y):
        #va mettre dans le tableau voisines les cellules qui sont vivante autour de la cellule donnée
        voisines = []
        for i in range(max(self.c.x-1,self.c.x),min(self.c.x+1,len(self.largeur))): #fait en sorte de pas calculer les cellules en dehors de la grille
            for j in range(max(self.c.y-1,self.c.y),min(self.c.y+1,len(self.hauteur))):  #fait en sorte de pas calculer les cellules en dehors de la grille
                if Cellule(i,j) == True:
                    voisines.append(Cellule(i,j))


    def tour(self):
        pass
        

    def remplir(self):
        pass

    def afficher(self):
        pass
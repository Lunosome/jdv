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
import pyxel

class interface:

    def __init__(self):
        pyxel.init(128,128, title="Jeu de la vie")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass

    def draw(self):
        pass



interface()
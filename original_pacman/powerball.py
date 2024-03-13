from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class Powerball(Widget):
    image = StringProperty('img/circle.png')

    def collide_player(self, player):
        if self.x - 10 <= player.pos[0] and self.x+10>= player.pos[0] and self.y - 30 == player.pos[1]:
            return True
        else:
            return False
    
    

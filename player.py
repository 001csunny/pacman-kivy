from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector


bound = {}
bound[1] = (0, 164.5)
bound[11] = (77, 164.5)
bound[2] = (1123, 164.5)

bound[3] = (565, 164.5)
bound[4] = (565, 323.5)

bound[5] = (565, 1.5)

bound[6] = (77, 274)
bound[7] = (76, 47)

bound[8] = (77, 164.5)

bound[9] = (77, 46)
bound[10] = (1055, 47)

bound[12] = (157, 47)
bound[13] = (157, 275)
bound[14] = (157, 164.5)
bound[15] = (1055, 164.5)

bound[16] = (1055, 275)




# Passage list
passages = []
passages = [
    bound[1] + bound[11],
    bound[3] + bound[4],
    bound[5] + bound[3],
    bound[8] + bound[6],
    bound[7] + bound[8],
    bound[9] + bound[10],
    bound[12] + bound[13],
    bound[13] + bound[14],
    bound[14] + bound[15],
    bound[6] + bound[16],
]


class Player(Widget):
    pac_img = StringProperty("img/boy_right.gif")
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    elan = (0, 0)

    def move(self):

        last_pos = self.pos.copy()
        # print(self.pos)

        for passage in passages:
            if (
                (passage[0] <= self.velocity_x + self.pos[0])
                and (passage[2] >= self.velocity_x + self.pos[0])
                and (passage[1] <= self.velocity_y + self.pos[1])
                and (passage[3] >= self.velocity_y + self.pos[1])
            ):

                self.pos = Vector(*self.velocity) + self.pos
                self.elan = self.velocity.copy()

                if self.velocity == [0, 1]:
                    self.pac_img = "img/boy_up.gif"
                elif self.velocity == [0, -1]:
                    self.pac_img = "img/boy_down.gif"
                elif self.velocity == [-1, 0]:
                    self.pac_img = "img/boy_left.gif"
                elif self.velocity == [1, 0]:
                    self.pac_img = "img/boy_right.gif"

        if self.pos == last_pos:
            for passage in passages:
                if (
                    (passage[0] - 0.1 <= self.elan[0] + self.pos[0])
                    and (passage[2] + 0.1 >= self.elan[0] + self.pos[0])
                    and (passage[1] - 0.1 <= self.elan[1] + self.pos[1])
                    and (passage[3] + 0.1 >= self.elan[1] + self.pos[1])
                ):
                    self.pos = Vector(*self.elan) + self.pos

        if self.pos == [bound[1][0], (bound[1][1])]:
            self.pos = [bound[2][0], (bound[2][1])]

        elif self.pos == [bound[2][0], (bound[2][1])]:
            self.pos = [bound[1][0], (bound[1][1])]
        
        if self.pos == [bound[5][0], (bound[5][1])]:
            self.pos = [bound[4][0], (bound[4][1])]

        elif self.pos == [bound[4][0], (bound[4][1])]:
            self.pos = [bound[5][0], (bound[5][1])]

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector


close_list = [[11,12],[3,29],[3,30],[13,11]]


bound = {}
bound[1] = (0, 164.5)
bound[11] = (77, 164.5)
bound[2] = (1123, 164.5)

bound[3] = (1056, 164.5)
bound[4] = (1123, 164.5)

# bound[5] = (565, 1.5)

bound[6] = (77, 274)
bound[7] = (77, 48)

# bound[8] = (77, 164.5)

#bound[9] = (77, 48)
bound[10] = (1055, 49)

bound[12] = (157, 49)
bound[13] = (157, 274)
bound[14] = (157, 164.5)
bound[15] = (231.5, 164.5)

bound[16] = (1055, 275)

bound[17] = (232, 49)
bound[18] = (232, 274)

bound[19] = (436, 49)
bound[20] = (436, 274)

bound[21] = (436, 172.5)
bound[22] = (362, 172.5)

bound[23] = (565, 49)
bound[24] = (565, 0)
bound[25] = (565, 274)
bound[26] = (565, 332)

bound[27] = (745, 49)
bound[28] = (745, 274)

bound[29] = (981, 49)
bound[30] = (981, 274)

bound[31] = (852, 139)
bound[32] = (981, 140)


# Passage list
passages = []
passages = [
    bound[1] + bound[11],
    bound[3] + bound[4],
    # bound[5] + bound[3],
    bound[11] + bound[6],
    bound[7] + bound[11],
    bound[7] + bound[10],
    bound[12] + bound[13],
    bound[13] + bound[14],
    bound[14] + bound[15],
    bound[6] + bound[16],
    bound[10] + bound[16],
    bound[17] + bound[18],
    bound[19] + bound[20],
    bound[22] + bound[21],
    bound[24] + bound[23],
    bound[25] + bound[26],
    bound[27] + bound[28],
    bound[29] + bound[32],
    bound[32] + bound[30],
    bound[31] + bound[32],
]


class Player(Widget):
    pac_img = StringProperty("img/boy_right.gif")
    score = NumericProperty(0)
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

        if self.pos == [bound[26][0], (bound[26][1])-0.5]:
            self.pos = [bound[24][0], (bound[24][1]+0.5)]

        elif self.pos == [bound[24][0], (bound[24][1])+0.5]:
            self.pos = [bound[26][0], (bound[26][1]-0.5)]
        
        if self.pos == [bound[1][0], (bound[1][1])]:
            self.pos = [bound[4][0], (bound[4][1])]

        elif self.pos == [bound[4][0], (bound[4][1])]:
            self.pos = [bound[1][0], (bound[1][1])]

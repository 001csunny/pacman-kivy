from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from original_pacman.gostBrain import pts_graph, distance, argmin



close_list = [[2,4],[1,30],[29,4],[3,1],[30,9],[8,30],[29,25],[6,10,13],[5,14,10],[11,9,8],\
              [10,14,13],[29,26],[8,14,15],[9,13,16],[13,17,19],[14,21,17],[18,16,15],[17],[15,23,20],[19,22],\
                [16,22,24],[20,21],[24,19,25],[21,23,26],[28,23,7],[24,12,28],[28],[27,26,25],[3,12,7],[5,6,2]]


bound = {}
bound[1] = (0, 164)
bound[2] = (76, 164) # bound[11]
bound[3] = (1056, 164)
bound[4] = (1123, 164)
bound[5] = (77, 274) # bound[6]
bound[6] = (77, 48) # bound[7]
bound[7] = (1055, 49) # bound[10]
bound[8] = (157, 49) # bound[12]
bound[9] = (157, 273) # bound[13]
bound[10] = (157, 164) # bound[14]
bound[11] = (232, 164) # bound[15]
bound[12] = (1055, 275) # bound[16]
bound[13] = (233, 49) # bound[17]
bound[14] = (233, 274) # bound[18]
bound[15] = (436, 49) # bound[19]
bound[16] = (436, 274) # bound[20]
bound[17] = (436, 172) # bound[21]
bound[18] = (362, 172) # bound[22]
bound[19] = (565, 49) # bound[23]
bound[20] = (565, 0) # bound[24]
bound[21] = (565, 274) # bound[25]
bound[22] = (565, 332) # bound[26]
bound[23] = (745, 49) # bound[27]
bound[24] = (745, 274) # bound[28]
bound[25] = (981, 49) # bound[29]
bound[26] = (981, 274) # bound[30]
bound[27] = (852, 139) # bound[31]
bound[28] = (981, 140) # bound[32]
bound[29] = (1055, 165)
bound[30] = (77, 165)
# Passage list

passages = [
    bound[1] + bound[2],
    bound[3] + bound[4],
    # bound[5] + bound[3],
    bound[6] + bound[5],

    bound[6] + bound[7],
    bound[8] + bound[9],
 
    bound[10] + bound[11],
    bound[5] + bound[12],
    bound[7] + bound[12],
  
    bound[29] + bound[3],
    bound[13] + bound[14],
    bound[15] + bound[16],
    bound[18] + bound[17],
    bound[20] + bound[19],
    bound[21] + bound[22],
    bound[23] + bound[24],
    bound[25] + bound[28],
    bound[28] + bound[26],
    bound[27] + bound[28],
]

graph = pts_graph(close_list,bound)
class Player(Widget):
    pac_img = StringProperty("img/boy_right.gif")
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    

    elan = (0, 0)
    close_point = 1
    def move(self):

        last_pos = self.pos.copy()
      

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

        if self.pos == [bound[22][0], (bound[22][1])-0.5]:
            self.pos = [bound[20][0], (bound[20][1]+0.5)]

        elif self.pos == [bound[20][0], (bound[20][1])+0.5]:
            self.pos = [bound[22][0], (bound[22][1]-0.5)]
        
        if self.pos == [bound[1][0], (bound[1][1])]:
            self.pos = [bound[4][0], (bound[4][1])]

        elif self.pos == [bound[4][0], (bound[4][1])]:
            self.pos = [bound[1][0], (bound[1][1])]


        self.close_point = \
            argmin(lambda x:distance(self.pos, bound[x]),close_list[self.close_point -1], self.close_point)

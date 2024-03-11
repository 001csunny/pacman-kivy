from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

from random import randint
from math import *
from food import *

from player import  graph, close_list


from gostBrain import dijkstra, distance, argmin

bound = {}
bound[1] = (0, 164)
bound[2] = (77, 164) # bound[11]
bound[3] = (1055, 164)
bound[4] = (1123, 164)
bound[5] = (77, 273) # bound[6]
bound[6] = (77, 48) # bound[7]
bound[7] = (1055, 49) # bound[10]
bound[8] = (158, 49) # bound[12]
bound[9] = (158, 272) # bound[13]
bound[10] = (158, 164) # bound[14]
bound[11] = (232, 164) # bound[15]
bound[12] = (1055, 273) # bound[16]
bound[13] = (233, 49) # bound[17]
bound[14] = (233, 272) # bound[18]
bound[15] = (435, 49) # bound[19]
bound[16] = (435, 273) # bound[20]
bound[17] = (435, 172) # bound[21]
bound[18] = (362, 172) # bound[22]
bound[19] = (565, 49) # bound[23]
bound[20] = (565, 0) # bound[24]
bound[21] = (565, 273) # bound[25]
bound[22] = (565, 332) # bound[26]
bound[23] = (745, 49) # bound[27]
bound[24] = (745, 273) # bound[28]
bound[25] = (981, 49) # bound[29]
bound[26] = (981, 273) # bound[30]
bound[27] = (852, 140) # bound[31]
bound[28] = (981, 140) # bound[32]


passages = [
    bound[1] + bound[2],
    bound[3] + bound[4],
   
    bound[6] + bound[5],
    bound[6] + bound[7],
    bound[8] + bound[9],
    bound[10] + bound[11],
    bound[5] + bound[12],
    bound[7] + bound[12],
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
class Ghost(Widget):

    sp = StringProperty('img/ghost01.gif')

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(-1)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    elan = (0, 0)

    strat = (0, [])

    close_point = 26

    def move(self, randomly=True):

        last_pos = self.pos.copy()
        print(self.pos)
        for passage in passages:
            if (passage[0] <= self.velocity_x + self.pos[0]) and \
               (passage[2] >= self.velocity_x + self.pos[0]) and \
               (passage[1] <= self.velocity_y + self.pos[1]) and \
               (passage[3] >= self.velocity_y + self.pos[1]):

                self.pos = Vector(*self.velocity)+self.pos
                self.elan = self.velocity.copy()

                if self.velocity == [-1, 0]:
                    self.sp = 'img/ghost01.gif'

                if self.velocity == [1, 0]:
                    self.sp = 'img/ghost01.gif'
                if self.velocity == [0, -1]:
                    self.sp = 'img/ghost01.gif'

                if self.velocity == [0, 1]:
                    self.sp = 'img/ghost01.gif'


        if self.pos == last_pos:
            for passage in passages:
                if (
                    (passage[0] - 0.1 <= self.elan[0] + self.pos[0])
                    and (passage[2] + 0.1 >= self.elan[0] + self.pos[0])
                    and (passage[1] - 0.1 <= self.elan[1] + self.pos[1])
                    and (passage[3] + 0.1 >= self.elan[1] + self.pos[1])
                ):
                    self.pos = Vector(*self.elan)+self.pos

        # How about making our pacman dissapear on one side and come out the other
        if self.pos == [bound[22][0], (bound[22][1])]:
            self.pos = [bound[20][0], (bound[20][1])]

        elif self.pos == [bound[20][0], (bound[20][1])]:
            self.pos = [bound[22][0], (bound[22][1])]

        if self.pos == [bound[1][0], (bound[1][1])]:
            self.pos = [bound[4][0], (bound[4][1])]

        elif self.pos == [bound[4][0], (bound[4][1])]:
            self.pos = [bound[1][0], (bound[1][1])]

        if self.pos == last_pos:
            if (self.strat[1] == [] or randomly) and ((self.pos[0], self.pos[1]) in bound):
                self.direction()
                self.move()

        self.close_point = \
            argmin(lambda x: distance(
                self.pos, bound[x]), close_list[self.close_point - 1], self.close_point)

    def direction(self):
        dep = randint(0, 3)
        if dep == 0:
            self.velocity = (-1, 0)
        if dep == 1:
            self.velocity = (1, 0)
        if dep == 2:
            self.velocity = (0, 1)
        if dep == 3:
            self.velocity = (0, -1)

    def strategy(self):

        try:
            if (self.pos[0], self.pos[1]) == bound[self.strat[1][0]]:
                self.strat = (self.strat[0], self.strat[1][1::])

            if (bound[self.strat[1][0]][1] - self.pos[1]) != 0:
                self.velocity = [0, (bound[self.strat[1][0]][1] - self.pos[1]) /
                                 abs(bound[self.strat[1][0]][1] - self.pos[1])]

            if (bound[self.strat[1][0]][0] - self.pos[0]) != 0:
                self.velocity = [(bound[self.strat[1][0]][0] - self.pos[0]) /
                                 abs(bound[self.strat[1][0]][0] - self.pos[0]), 0]
            self.move(False)
        except:
            self.move()

    def next_strategy(self, close_to_player):
        self.strat = dijkstra(self.close_point, close_to_player, graph)

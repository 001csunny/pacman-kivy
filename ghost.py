from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

from random import randint
from math import *
from food import *

from player import passages, bound ,graph,close_list

from gostBrain import dijkstra, distance, argmin

class Ghost(Widget):
    sp = StringProperty('img/ghost01.gif')

    velocity_x = NumericProperty(1)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    elan = (0, -1)

    strat = (0, [])

    def move(self, randomly=True):

        last_pos = self.pos.copy()

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

        if self.pos == last_pos:
            for passage in passages:
                if (passage[0] - 0.1 <= self.elan[0] + self.pos[0]) and \
                   (passage[2] + 0.1 >= self.elan[0] + self.pos[0]) and \
                   (passage[1] - 0.1 <= self.elan[1] + self.pos[1]) and \
                   (passage[3] + 0.1 >= self.elan[1] + self.pos[1]):
                    self.pos = Vector(*self.elan)+self.pos

        if self.pos == [bound[26][0], (bound[26][1])-0.5]:
            self.pos = [bound[24][0], (bound[24][1]+0.5)]

        elif self.pos == [bound[24][0], (bound[24][1])+0.5]:
            self.pos = [bound[26][0], (bound[26][1]-0.5)]
        
        if self.pos == [bound[1][0], (bound[1][1])]:
            self.pos = [bound[4][0], (bound[4][1])]

        elif self.pos == [bound[4][0], (bound[4][1])]:
            self.pos = [bound[1][0], (bound[1][1])]

        if self.pos == last_pos:
            if (self.strat[1] == [] or randomly) and ((self.pos[0], self.pos[1]) in bound):
                self.direction()
                self.move()
        
        self.close_point = \
             argmin(lambda x:distance(self.pos, bound[x]),close_list[self.close_point -1], self.close_point)

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
        # lets actually make our ghost follow player
        try:
            if (self.pos[0], self.pos[1]) == bound[self.strat[1][0]]:
                self.strat = (self.strat[0], self.strat[1][1::])

            # error change strat to pos

            if (bound[self.strat[1][0]][1] - self.pos[1]) != 0:
                self.velocity = [0,(bound[self.strat[1][0]][1] - self.pos[1] ) / abs(bound[self.strat[1][0]][1] - self.pos[1])]
                
            if (bound[self.strat[1][0]][0] - self.pos[0]) != 0:
                self.velocity = [(bound[self.strat[1][0]][0] - self.pos[0] ) / abs(bound[self.strat[1][0]][0] - self.pos[0]),0]
            self.move(False)
        except:
            self.move()
    
    def next_strategy(self, close_to_player):
        self.strat = dijkstra(self.close_point, close_to_player, graph)
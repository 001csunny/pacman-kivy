from kivy.uix.widget import Widget
from original_pacman.player import passages

food = []

for a0, a1, b0, b1 in passages:
    if a0==b0:
        for j in range(int(a1)+20, int(b1)-20,20):
            food.append([a0 + 38.5, j + 38.5])
    
    else:
        for j in range(int(a0),int(b0),20):
            food.append([j + 38.5, a1 + 38.5])

food = food[:191]

eaten = [i for i in range(len(food)) if i not in [179]]


class Points(Widget):
    print('this is food')

from heapq import *
import math


def distance(pointA, pointB):
    return math.sqrt((pointA[0]-pointB[0])**2+(pointA[1]-pointB[1])**2)

def argmin(f, l, j):
    arg = j
    for i in range(len(l)):
        if f(l[i]) < f(arg):
            arg = l[i]
    return arg


def dijkstra(s,t,graph):
    M = set()
    d = {s: 0}
    p = {}
    following = [(0, s)]

    while following != []:

        dx, x = heappop(following)
        if x in M:
            continue

        M.add(x)

        for w,y in nearby(x,graph):
            if y in M:
                continue
            dy = dx + w
            if y not in d or d[y] > dy:
                d[y] = dy
                heappush(following, (dy, y))
                p[y] = x

    path = [t]
    x = t
    while x != s:
        x = p[x]
        path.insert(0,x)

    return d[t], path

def nearby(s,graph):
    return graph[s]

def pts_graph(the_close_list, the_points_list):
    gr={}
    for i in range(1, len(the_close_list)+1):
        gr[i]=[]
        for j in the_close_list[i-1]:
            gr[i].append((distance(the_points_list[j],the_points_list[i]), j))
    return(gr)
    

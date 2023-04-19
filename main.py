import heapq as hq
import time
import queue 
from collections import deque



def BFS (initial_state):
    class Node:
        def __init__(self, state, parent, level):
            self.state = state
            self.level = level
            self.parent = parent
    
    nodes_expanded = 0
    nodes_generated = 0
    
    # queue 
    nodes_list = deque()
    states_list = deque()

    init_node = Node(initial_state,None,0)

    nodes_list.append(init_node)
    states_list.append(initial_state)

    # set of visited states
    explored = set()

    while states_list:
        node = nodes_list.popleft()
        state = states_list.popleft()
        explored.add(tuple(node.state))
        nodes_expanded+=1

        print(state)

        if goalTest(state):
            print("found Goal")
            return [nodes_expanded, node.level, nodes_generated, node]

        for neighbor in findNeighbours(state):
            if tuple(neighbor) not in explored:
                nodes_generated+=1
                new_node = Node(neighbor,node,node.level+1)
                nodes_list.append(new_node)
                states_list.append(neighbor)
                explored.add(tuple(neighbor))
    
    print("out")

    return None


def DFS (initial_state):
    class Node:
        def __init__(self, state, parent, level):
            self.state = state
            self.level = level
            self.parent = parent
    
    nodes_expanded = 0
    nodes_generated = 0
    
    # queue 
    nodes_list = []
    states_list = []

    init_node = Node(initial_state,None,0)

    nodes_list.append(init_node)
    states_list.append(initial_state)

    # set of visited states
    explored = set()

    while states_list:
        node = nodes_list.pop()
        state = states_list.pop()
        explored.add(tuple(state))
        nodes_expanded+=1

        print(state)

        if goalTest(state):
            print("found Goal")
            return [nodes_expanded, node.level, nodes_generated, node]

        for neighbor in findNeighbours(state):
            if tuple(neighbor) not in explored:
                nodes_generated+=1
                new_node = Node(neighbor,node,node.level+1)
                nodes_list.append(new_node)
                states_list.append(neighbor)
                explored.add(tuple(neighbor))
    
    print("out")

    return None

def goalTest(state):
    if state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return True
    return False
    

def AManhattan (initial_state):
    
    class Node:
        def __init__(self, state, value, parent,level):
            self.state = state
            self.value = value
            self.parent = parent
            self.level = level
    
    nodes_expanded = 0
    nodes_generated = 0
    
    nodes_list = []
    states_list_values = []

    init_node = Node(initial_state,computeHeuristic(initial_state, 'M'),None,0)

    nodes_list.append(init_node)
    states_list_values.append(init_node.value)

    hq.heapify(states_list_values)
    # set of visited states
    explored = set()

    while len(states_list_values) != 0:
        state_value = hq.heappop(states_list_values)
        state = []
        tmp_node = None
        for v in nodes_list:     
            if v.value == state_value:
                state = v.state
                tmp_node = v
        nodes_list.remove(tmp_node)
             
        explored.add(tuple(state))
        nodes_expanded+=1

        if goalTest(list(state)):
            print("found Goal")
            return [nodes_expanded, tmp_node.level, nodes_generated, tmp_node]

        for neighbor in findNeighbours(state):
            if neighbor not in nodes_list and tuple(neighbor) not in explored:
                nodes_generated+=1
                hq.heappush(states_list_values, computeHeuristic(neighbor,'M')+tmp_node.level+1)
                new_node = Node(neighbor,computeHeuristic(neighbor, 'M')+tmp_node.level+1
                                ,tmp_node,tmp_node.level+1)
                nodes_list.append(new_node)


    return None

def AEuclidean (initial_state):
    
    class Node:
        def __init__(self, state, value, parent,level):
            self.state = state
            self.value = value
            self.parent = parent
            self.level = level
    
    nodes_expanded = 0
    nodes_generated = 0
    
    nodes_list = []
    states_list_values = []

    init_node = Node(initial_state,computeHeuristic(initial_state, 'E'),None,0)

    nodes_list.append(init_node)
    states_list_values.append(init_node.value)

    hq.heapify(states_list_values)
    # set of visited states
    explored = set()

    while len(states_list_values) != 0:
        state_value = hq.heappop(states_list_values)
        state = []
        tmp_node = None
        for v in nodes_list:     
            if v.value == state_value:
                state = v.state
                tmp_node = v
        nodes_list.remove(tmp_node)
             
        explored.add(tuple(state))
        nodes_expanded+=1

        if goalTest(list(state)):
            print("found Goal")
            return [nodes_expanded, tmp_node.level, nodes_generated, tmp_node]

        for neighbor in findNeighbours(state):
            if neighbor not in nodes_list and tuple(neighbor) not in explored:
                nodes_generated+=1
                hq.heappush(states_list_values, computeHeuristic(neighbor,'E')+tmp_node.level+1)
                new_node = Node(neighbor,computeHeuristic(neighbor, 'E')+tmp_node.level+1
                                ,tmp_node,tmp_node.level+1)
                nodes_list.append(new_node)


    return None


def visualize_path(state):
    for i in range(0,9,3):
        print(state[i],state[i+1],state[i+2])
        print("\n")
    print("============")


def trace_path(node):
    cost = 0
    path = []
    while(node.parent != None):
        path.append(node.state)
        node = node.parent
        cost+=1
    path.append(node.state)
    path.reverse()
    for p in path:
        visualize_path(p)
    return cost

def computeHeuristic (state, type):
    # Manhattan distance heuristic
    if type == 'M':
        distance = 0
        for i in range(9):
            if state[i] != 0:
                distance += abs(i // 3 - state[i] // 3) + abs(i % 3 - state[i] % 3)
        return distance
    
    # Eucledian distance heuristic
    elif type == 'E':
        distance = 0
        for i in range(9):
            if state[i] != 0:
                distance += ((i // 3 - state[i] // 3) ** 2 + (i % 3 - state[i] % 3) ** 2) ** 0.5
        return distance

def checlSolvable(state):
    invCount = 0
    for i in range(0,8):
        for j in range(i+1,9):
            if state[j] != 0 and state[i] != 0 and state[i] > state[j]:
                invCount+=1
    return (invCount % 2 == 0)

def findNeighbours(state):
    res = []
    ind = state.index(0)
    if not top(ind):
        res.append(up_neig(state, ind))
    if not bottom(ind):
        res.append(down_neig(state, ind))
    if not left(ind):
        res.append(left_neig(state, ind))
    if not right(ind):
        res.append(right_neig(state, ind))
    return res

def top(ind):
    return ind < 3

def bottom(ind):
    return ind > 5

def left(ind):
    return ind in [0, 3, 6]

def right(ind):
    return ind in [2, 5, 8]

def up_neig(p, ind):
    _p = list(p)
    _p[ind], _p[ind-3] = _p[ind-3], _p[ind]
    return tuple(_p)

def down_neig(p, ind):
    _p = list(p)
    _p[ind], _p[ind+3] = _p[ind+3], _p[ind]    
    return tuple(_p)

def left_neig(p, ind):
    _p = list(p)
    _p[ind], _p[ind-1] = _p[ind-1], _p[ind]
    return tuple(_p)

def right_neig(p, ind):
    _p = list(p)
    _p[ind], _p[ind+1] = _p[ind+1], _p[ind]
    return tuple(_p)


if __name__ == '__main__':
    
    print("Enter Puzzle initial state: (9 numbers from 0 to 8 with each number present only once)")
    initial_state = str(input())
    initial_state_array = [int(x) for x in initial_state]

    if (not(checlSolvable(initial_state_array))):
        print("the puzzle is unsolvable")
        exit()

    print("Choose the preffered algorithm: (1) BFS (2) DFS (3) A*(Manhattan) (4) A*(Euclidean)")
    choice = int(input())
    if (choice == 1):
        st = time.time()
        output = BFS(initial_state_array)
        et = time.time()
    elif (choice == 2):
        st = time.time()
        output = DFS(initial_state_array)
        et = time.time()
    elif (choice == 3):
        st = time.time()
        output = AManhattan(initial_state_array)
        et = time.time()
    elif (choice == 4):
        st = time.time()
        output = AEuclidean(initial_state_array)
        et = time.time()
    else:
        print("invalid choice")

    cost = trace_path(output[3])
    print("cost: ", cost, "moves")
    print("nodes expanded: ", output[0], "nodes")
    print("search depth: ", output[1], "nodes")
    print("nodes generated: ", output[2], "nodes")
    print("running time: ", (et-st)*1000, "ms")


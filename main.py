import heapq as hq


def BFS (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    
    return [cost, nodes_expanded, search_depth, running_time]

# add it to your node structure
def goalTest(state):
    if state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return True
    return False
    

def DFS (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    
    return [cost, nodes_expanded, search_depth, running_time]

def AManhattan (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0

    



    
   
    return [cost, nodes_expanded, search_depth, running_time]

def AEuclidean (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0


    return [cost, nodes_expanded, search_depth, running_time]


def visualize_path(state):
    for i in range(0,9,3):
        print(state[i],state[i+1],state[i+2])
        print("\n")
    print("=====")


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
        output = BFS(initial_state_array)
    elif (choice == 2):
        output = DFS(initial_state_array)
    elif (choice == 3):
        output = AManhattan(initial_state_array)
    elif (choice == 4):
        output = AEuclidean(initial_state_array)
    else:
        print("invalid choice")

    print("cost: ", output[0])
    print("nodes expanded: ", output[1])
    print("search depth: ", output[2])
    print("running time: ", output[3])


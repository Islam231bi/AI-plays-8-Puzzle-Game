def BFS (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    return [cost, nodes_expanded, search_depth, running_time]

def DFS (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    return [cost, nodes_expanded, search_depth, running_time]

def AManhattan (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]


   
    return [cost, nodes_expanded, search_depth, running_time]

def AEuclidean (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    return [cost, nodes_expanded, search_depth, running_time]


def visualize_path(state):
    for i in range(0,9,3):
        print(state[i],state[i+1],state[i+2])
        print("\n")
    print("=====")


def computeHeuristic (state, type):
    value = 0
    if type == 'M':
        pass
    elif type == 'E':
        pass

    return value

def checlSolvable(state):
    invCount = 0
    for i in range(0,8):
        for j in range(i+1,9):
            if state[j] != 0 and state[i] != 0 and state[i] > state[j]:
                invCount+=1
    return (invCount % 2 == 0)




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
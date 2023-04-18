from queue import PriorityQueue
import queue

def BFS (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    return [cost, nodes_expanded, search_depth, running_time]

def goalTest(state):
    if state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return True
    return False

def DFS(initial_state):
    frontier = queue.LifoQueue()
    frontier.put(initial_state)
    frontier_config = {}
    frontier_config[tuple(initial_state.config)] = True
    explored = set()
    nodes_expanded = 0
    max_search_depth = 0

    while not frontier.empty():
        state = frontier.get()
        print("****** State ******")
        state.display()
        explored.add(state.config)
        if state.goalTest():
            return (state,nodes_expanded,max_search_depth)
        
        nodes_expanded += 1
        for neighbor in state.expand():
            if neighbor.config not in explored and tuple(neighbor.config) not in frontier_config:   
                frontier.put(neighbor)
                frontier_config[tuple(neighbor.config)] = True
                if neighbor.cost > max_search_depth:
                    max_search_depth = neighbor.cost
    return None

# def DFS (initial_state):
#     cost = 0
#     nodes_expanded = 0
#     search_depth = 0
#     running_time = 0
#     goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
#     return [cost, nodes_expanded, search_depth, running_time]

def AManhattan (initial_state):
    cost = 0
    nodes_expanded = 0
    search_depth = 0
    running_time = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Define the node class to store the state, parent node, and cost
    class Node:
        def __init__(self, state, parent=None, cost=0):
            self.state = state
            self.parent = parent
            self.cost = cost

        def __lt__(self, other):
            return self.cost + computeHeuristic(self.state, 'M') < other.cost + computeHeuristic(other.state, 'M')

    # Initialize the frontier with the initial node
    frontier = PriorityQueue()
    frontier.put(Node(initial_state))

    # Initialize the explored set
    explored = set()

    # Loop until the frontier is empty
    while not frontier.empty():
        # Get the node with the lowest cost
        node = frontier.get()

        # Check if the node is the goal state
        if node.state == goal_state:
            # If it is, trace back to the root node and return the path
            path = []
            while node.parent is not None:
                path.append(node.state)
                node = node.parent
            path.append(initial_state)
            return list(reversed(path))

        # Add the node to the explored set
        explored.add(tuple(node.state))

        # Generate the child nodes and add them to the frontier
        blank_index = node.state.index(0)
        for action in [-3, -1, 1, 3]:
            new_index = blank_index + action
            if 0 <= new_index < 9 and (new_index // 3 == blank_index // 3 or abs(new_index - blank_index) == 1):
                new_state = node.state[:]
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                if tuple(new_state) not in explored:
                    new_node = Node(new_state, parent=node, cost=node.cost + 1)
                    frontier.put(new_node)
   
    # return [cost, nodes_expanded, search_depth, running_time]

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

    # print("cost: ", output[0])
    # print("nodes expanded: ", output[1])
    # print("search depth: ", output[2])
    # print("running time: ", output[3])

    print(output)

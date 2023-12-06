import heapq
import random

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return ((self.cost + self.heuristic) < (other.cost + other.heuristic))

def A_Star(start, goal, graph, heuristic):
    open_set = []
    closed_set = set()
    start_node = Node(start, cost=0, heuristic=heuristic(start, goal))
    heapq.heappush(open_set, start_node)
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == goal:
            return path(current_node)

        closed_set.add(current_node.state)

        for neighbor, step_cost in graph[current_node.state]:
            if neighbor in closed_set:
                continue

            g = current_node.cost + step_cost
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, current_node, None, g, h)

            if not is_node_in_open_set(open_set, neighbor_node):
                heapq.heappush(open_set, neighbor_node)

    return None

def path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path
def pathCost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]

        edge = None
        for neighbor, edge_cost in graph[current_node]:
            if neighbor == next_node:
                edge = edge_cost
                break

        if edge is not None:
            cost += edge
        else:
            raise ValueError(f"Edge not found between {current_node} and {next_node} in the graph.")

    return cost
def is_node_in_open_set(open_set, node):
    for n in open_set:
        if n.state == node.state and n < node:
            return True
    return False

random.seed(0)

graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('A', 3), ('D', 4)],
    'C': [('A', 2), ('D', 5), ('C', 2)],
    'D': [('B', 4), ('C', 5), ('E',1)],
    'E': [('D',1),('C',2)],
}

start_node = 'A'
goal_node = 'E'

def random_heuristic(node, goal):
    return random.randint(1, 10)


path = A_Star(start_node, goal_node, graph, random_heuristic)

if path:
    print("Path found:", path)
else:
    print("No path found.")

path_cost = pathCost(graph,path)
print("Path cost:", path_cost)
import random

graph_map = {
    'A': {'B':3,'C':6},
    'B': {'D':4},
    'C': {'D':2,'E':7},
    'D': {'F':5},
    'E': {'F':3},
    'F': {}
}

heur = {'A':9,'B':6,'C':5,'D':3,'E':4,'F':0}


def change_cost_randomly(g):
    n = random.choice(list(g.keys()))
    if g[n]:
        m = random.choice(list(g[n].keys()))
        g[n][m] = random.randint(1,10)
        print(f"Cost changed: {n}->{m} = {g[n][m]}")


def realtime_a_star(graph, start, goal):

    open_nodes = [(start, heur[start])]
    g_val = {start:0}
    parent = {start:None}
    closed_nodes = []

    while open_nodes:

        open_nodes.sort(key=lambda x: x[1])
        current, _ = open_nodes.pop(0)

        if current in closed_nodes:
            continue

        print("Processing:", current)
        closed_nodes.append(current)

        if current == goal:
            path=[]
            while current:
                path.append(current)
                current = parent[current]
            print("Path:", path[::-1])
            return

        if random.random() < 0.5:
            change_cost_randomly(graph)

        for neighbor in graph[current]:

            new_g = g_val[current] + graph[current][neighbor]
            f_score = new_g + heur[neighbor]

            if neighbor not in g_val or new_g < g_val[neighbor]:
                g_val[neighbor] = new_g
                parent[neighbor] = current
                open_nodes.append((neighbor,f_score))

    print("Goal not reachable")


realtime_a_star(graph_map,'A','F')

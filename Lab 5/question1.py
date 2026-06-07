class State:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0


def manhattan_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def greedy_search_maze(maze, start, goal):

    open_list = [State(start)]
    closed = set()

    rows, cols = len(maze), len(maze[0])

    while open_list:

        open_list.sort(key=lambda x: x.h)
        current = open_list.pop(0)

        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed.add(current.position)

        for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx, ny = current.position[0]+dx, current.position[1]+dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0 and (nx,ny) not in closed:
                    node = State((nx,ny), current)
                    node.h = manhattan_dist((nx,ny), goal)
                    open_list.append(node)

    return None


def visit_all_goals(maze, start, goal_list):

    current = start
    total_path = []

    while goal_list:

        goal_list.sort(key=lambda g: manhattan_dist(current, g))
        next_goal = goal_list.pop(0)

        path = greedy_search_maze(maze, current, next_goal)
        if path is None:
            return None

        total_path += path[:-1]
        current = next_goal

    total_path.append(current)
    return total_path


maze = [
    [0,0,0,1,0],
    [1,0,1,0,0],
    [0,0,0,0,1],
    [0,1,0,0,0],
    [0,0,1,0,0]
]

print("Route:", visit_all_goals(maze,(0,0),[(4,4),(2,2),(3,0)]))

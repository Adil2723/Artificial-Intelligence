graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}


class GoalBasedDLSAgent:
    def __init__(self, graph, goal, depth_limit):
        self.graph = graph
        self.goal = goal
        self.depth_limit = depth_limit

    def goal_test(self, state):
        return state == self.goal

    def dls(self, current, depth, path, visited):
        if self.goal_test(current):
            return path

        if depth == 0:
            return None

        visited.append(current)

        for neighbor in self.graph.get(current, []):
            if neighbor not in visited:
                result = self.dls(
                    neighbor,
                    depth - 1,
                    path + [neighbor],
                    visited
                )
                if result is not None:
                    return result

        visited.remove(current)
        return None

    def act(self, start):
        visited = []
        return self.dls(start, self.depth_limit, [start], visited)


print("----- Goal-Based DLS Agent -----")

agent = GoalBasedDLSAgent(graph, goal='G', depth_limit=3)
print("Depth Limit = 3")
print("Path Found:", agent.act('A'))

agent2 = GoalBasedDLSAgent(graph, goal='G', depth_limit=2)
print("\nDepth Limit = 2")
print("Path Found:", agent2.act('A'))


weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [],
    'F': [('G', 3)],
    'G': []
}


class UtilityBasedUCSAgent:
    def __init__(self, graph, goal):
        self.graph = graph
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def act(self, start):
        frontier = [(0, start, [start])]
        visited = {}

        while frontier:
            frontier.sort(key=lambda x: x[0])
            cost, current, path = frontier.pop(0)

            if self.goal_test(current):
                return path, cost

            if current in visited and visited[current] <= cost:
                continue

            visited[current] = cost

            for neighbor, step_cost in self.graph.get(current, []):
                frontier.append(
                    (cost + step_cost,
                     neighbor,
                     path + [neighbor])
                )

        return None


print("\n----- Utility-Based UCS Agent -----")

ucs_agent = UtilityBasedUCSAgent(weighted_graph, goal='G')
path, cost = ucs_agent.act('A')

print("Minimum Cost Path:", path)
print("Total Cost:", cost)

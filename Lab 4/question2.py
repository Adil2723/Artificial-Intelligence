distances = {
    (1, 2): 10, (2, 1): 10,
    (1, 3): 15, (3, 1): 15,
    (1, 4): 20, (4, 1): 20,
    (2, 3): 35, (3, 2): 35,
    (2, 4): 25, (4, 2): 25,
    (3, 4): 30, (4, 3): 30
}

cities = [1, 2, 3, 4]
start_city = 1

min_cost = float('inf')
best_route = []

def tsp(current_city, visited, current_cost, path):
    global min_cost, best_route

    if len(visited) == len(cities):
        total_cost = current_cost + distances[(current_city, start_city)]
        if total_cost < min_cost:
            min_cost = total_cost
            best_route = path + [start_city]
        return

    for city in cities:
        if city not in visited:
            cost = distances[(current_city, city)]
            visited.append(city)
            tsp(city, visited, current_cost + cost, path + [city])
            visited.remove(city)

tsp(start_city, [start_city], 0, [start_city])

print("Shortest Route:", best_route)
print("Minimum Cost:", min_cost)

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def route_planner(start, deliveries):

    current = start
    time_clock = 0
    path_taken = []

    pending = deliveries.copy()

    while pending:

        pending.sort(key=lambda x: x["end"])

        best_option = None
        min_distance = float('inf')

        for d in pending:
            travel = manhattan(current, d["loc"])
            arrival = time_clock + travel

            if arrival <= d["end"]:
                if travel < min_distance:
                    min_distance = travel
                    best_option = d

        if best_option is None:
            print("Time window violated!")
            return None

        travel = manhattan(current, best_option["loc"])
        time_clock += travel

        if time_clock < best_option["start"]:
            time_clock = best_option["start"]

        print(f"Delivered at {best_option['loc']} at {time_clock}")

        path_taken.append(best_option["loc"])
        current = best_option["loc"]
        pending.remove(best_option)

    print("Completed Route:", path_taken)
    return path_taken


deliveries = [
    {"loc":(3,4),"start":0,"end":9},
    {"loc":(5,1),"start":2,"end":7},
    {"loc":(6,6),"start":5,"end":14},
    {"loc":(2,8),"start":3,"end":6}
]

route_planner((0,0), deliveries)

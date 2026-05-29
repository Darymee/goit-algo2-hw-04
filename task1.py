from collections import deque, defaultdict

edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]


def edmonds_karp(edges, source, sink):
    capacity = defaultdict(lambda: defaultdict(int))
    graph = defaultdict(list)

    for u, v, c in edges:
        capacity[u][v] += c
        graph[u].append(v)
        graph[v].append(u)

    max_flow = 0
    steps = []

    while True:
        parent = {source: None}
        queue = deque([source])

        while queue and sink not in parent:
            u = queue.popleft()
            for v in graph[u]:
                if v not in parent and capacity[u][v] > 0:
                    parent[v] = u
                    queue.append(v)

        if sink not in parent:
            break

        path_flow = float("inf")
        v = sink
        path = []

        while parent[v] is not None:
            u = parent[v]
            path.append((u, v))
            path_flow = min(path_flow, capacity[u][v])
            v = u

        path.reverse()

        for u, v in path:
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow

        max_flow += path_flow
        steps.append((path, path_flow, max_flow))

    return max_flow, steps


source = "Джерело"
sink = "Сток"

network = edges.copy()

network += [
    ("Джерело", "Термінал 1", 10**9),
    ("Джерело", "Термінал 2", 10**9),
]

for i in range(1, 15):
    network.append((f"Магазин {i}", "Сток", 10**9))

max_flow, steps = edmonds_karp(network, source, sink)

print("Максимальний потік:", max_flow)

for i, (path, flow, total) in enumerate(steps, 1):
    route = " -> ".join([path[0][0]] + [v for _, v in path])
    print(f"{i}. {route}: +{flow}, сумарно {total}")

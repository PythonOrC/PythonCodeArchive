from path import Map


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"],
}


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = []
    seen.append(s)
    parent = {s: None}
    while queue:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.append(node)
                parent[node] = vertex
    return seen, parent


def shortest_path(parent, start, finish):
    path = []
    vertex = finish
    while vertex != start:
        path.append(vertex)
        vertex = parent[vertex]
    path.append(start)
    path.reverse()
    return path


map = Map()
map.map_init()
start = input("请输入起点：")
finish = input("请输入终点：")

visited, parent = BFS(graph, start)
if finish in visited:
    print("存在")
    path = shortest_path(parent, start, finish)
    map.show_route(path)
else:
    print("不存在")

map.finish()

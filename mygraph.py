class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def num_vertices(self):
        return len(self.__graph_dict)

    def edges(self):
        return self.__generate_edges()

    def num_edges(self):
        return len(self.__generate_edges())

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    graph = Graph(g)


N = 0
S = 0
GRAPH = []


with open(file="graph.txt", mode="r", encoding="utf-8") as file:
    for i, each_line in enumerate(file.readlines()):
        if i == 0:
            N = int(each_line.strip("\r\n").split(" ")[1])
        else:
            GRAPH.append([int(x) for x in each_line.strip("\r\n").split(" ")[:-1]])

print(N)
print(GRAPH)


def Dijkstra(N, S, matrix):
    valid = [True] * N
    weight = [1000000] * N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight


print(Dijkstra(N, S, GRAPH))

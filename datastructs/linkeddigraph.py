from edge import Edge
from edgenode import EdgeNode
from graph import Graph
from graphchain import GraphChain


class LinkedDiGraph(Graph):

    def output(self):
        for i in range(1, self.no_of_vertices + 1):
            print('Vertex %s = %s' % (i, self.adj_list[i]))

    def __init__(self, no_of_vertices=0):
        self.no_of_vertices = no_of_vertices
        self.no_of_edges = 0
        self.adj_list = []
        for trk in range(no_of_vertices + 1):
            self.adj_list.append(GraphChain())

    def put_edge(self, edge):
        v1 = edge.v1
        v2 = edge.v2
        # There was a check for permissible edge here
        edge_node = EdgeNode(v2)
        # The exist check is looking at wrong place
        if self.adj_list[v1].index_of(edge_node) == -1:
            self.adj_list[v1].add(0, edge_node)

    def get_edge_count(self):
        return self.no_of_edges


linked_di_graph = LinkedDiGraph(4)
print('Edges %s' % linked_di_graph.get_edge_count())
linked_di_graph.put_edge(Edge(2, 4))
linked_di_graph.put_edge(Edge(1, 3))
linked_di_graph.put_edge(Edge(2, 1))
linked_di_graph.put_edge(Edge(1, 4))
linked_di_graph.put_edge(Edge(4, 2))
print('The graph is ')
linked_di_graph.output()
# linked_di_graph.

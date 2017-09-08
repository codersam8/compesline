from edge import Edge
from edgenode import EdgeNode
from graph import Graph
from graphchain import GraphChain
from arrayqueue import ArrayQueue


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

    def breadth_first_search(self, v, reach, label):
        aq = ArrayQueue()
        reach[v] = label
        aq.put(v)
        while not aq.is_empty():
            w = aq.remove()
            p = self.adj_list[w].first_node
            while p:
                u = p.element.v
                if not reach[u]:
                    aq.put(u)
                    reach[u] = label
                p = p.next
        print(reach)

    def rec_depth_first_search(self, vert):
        self.reach[vert] = self.label
        curr_vert = self.adj_list[vert].first_node
        while curr_vert:
            if curr_vert:
                if self.reach[curr_vert.element.v] == 0:
                    self.reach[curr_vert.element.v] = self.label
                    self.rec_depth_first_search(curr_vert.element.v)
            curr_vert = curr_vert.next

    def depth_first_search(self, vert, reach, label):
        self.reach = reach
        self.label = label
        self.reach[vert] = self.label
        self.rec_depth_first_search(vert)
        print(self.reach)


linked_di_graph = LinkedDiGraph(10)
# print('Edges %s' % linked_di_graph.get_edge_count())
# linked_di_graph.put_edge(Edge(2, 4))
# linked_di_graph.put_edge(Edge(1, 3))
# linked_di_graph.put_edge(Edge(2, 1))
# linked_di_graph.put_edge(Edge(1, 4))
# linked_di_graph.put_edge(Edge(4, 2))
# print('The graph is ')
# linked_di_graph.output()
# linked_di_graph.

print('Edges %s' % linked_di_graph.get_edge_count())
def graph1():
    linked_di_graph.put_edge(Edge(1, 2))
    linked_di_graph.put_edge(Edge(1, 3))
    linked_di_graph.put_edge(Edge(1, 4))
    linked_di_graph.put_edge(Edge(2, 5))
    linked_di_graph.put_edge(Edge(3, 5))
    linked_di_graph.put_edge(Edge(4, 3))
    linked_di_graph.put_edge(Edge(4, 6))
    linked_di_graph.put_edge(Edge(4, 7))
    linked_di_graph.put_edge(Edge(5, 8))
    linked_di_graph.put_edge(Edge(6, 8))
    linked_di_graph.put_edge(Edge(6, 3))
    linked_di_graph.put_edge(Edge(7, 8))
    linked_di_graph.put_edge(Edge(7, 9))
    linked_di_graph.put_edge(Edge(10, 8))
    linked_di_graph.put_edge(Edge(10, 9))
    reach = [0] * 11
    linked_di_graph.breadth_first_search(2, reach, 1)
    linked_di_graph.depth_first_search(2, reach, 1)


def graph2():
    linked_di_graph.put_edge(Edge(1, 2))
    linked_di_graph.put_edge(Edge(1, 4))
    linked_di_graph.put_edge(Edge(2, 3))
    reach = [0] * 5
    linked_di_graph.depth_first_search(2, reach, 1)
    # print('The graph is ')
    # linked_di_graph.output()

graph2()

class LinkedDiGraph(Graph):

    def __init__(self):
        self.no_of_vertices = 0
        self.no_of_edges = 0

    def __init__(self, no_of_vertices):
        self.no_of_vertices = no_of_vertices
        graph_chain = GraphChain(no_of_vertices + 1)

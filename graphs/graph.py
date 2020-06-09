class Graph:
    def __init__(self):
        self.vertex = []
        self.final_graph = []

    def add_vertex(self,vertex_val):
        self.vertex.append(vertex_val)
        self.final_graph.append(vertex_val)

    def add_edge(self,from_vertex,to_vertex):
        if from_vertex and to_vertex in self.vertex:
            try:
                pos_to_vrtx = self.final_graph.index(to_vertex)
                self.final_graph.insert(pos_to_vrtx,f"{from_vertex}:{to_vertex}")
                pos_from_vrtx = self.final_graph.index(from_vertex)
                self.final_graph.pop(pos_from_vrtx)
            except ValueError:
                pass

    def display_graph(self):
        print(self.final_graph)
        return


# g = Graph()
# #Add vertex
# g.add_vertex("a")
# g.add_vertex("b")
# g.add_vertex("c")
# g.add_vertex("d")
# g.add_vertex("e")

# #Connect edges
# g.add_edge("a","c")
# g.add_edge("b","c")
# g.add_edge("b","e")
# g.add_edge("c","a")
# g.add_edge("c","b")
# g.add_edge("c","d")
# g.add_edge("b","e")
# g.add_edge("e","d")

# #display graph
# g.display_graph()
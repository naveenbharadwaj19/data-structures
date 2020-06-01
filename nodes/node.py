class Nodes:
    def __init__(self,value = None):
        self.value = value
        self.link_node = ""

    def add_val(self,value):
        self.value = value
        return self.value

    def add_nodes_link(self,val):
        val = self.add_val(val)
        if not self.link_node:
            self.link_node = f"{self.value}->"
            return self.link_node
        elif self.link_node:
            self.link_node += f"{val}->"
            return self.show_nodes()

    def show_nodes(self):
        if self.link_node[-2:] == "->":
            rem = self.link_node[:-2]
            return rem
    
    def remove_nodes(self,value:str) -> str:
        if self.link_node:
            self.link_node = self.link_node.replace(value + "->","",1)
            return self.show_nodes()
        else:
            return None


# nodes = Nodes()
# # add nodes
# #add_node_line
# nodes.add_nodes_link(20)
# nodes.add_nodes_link(25)
# nodes.add_nodes_link(30)
# nodes.add_nodes_link(35)
# #remove nodes
# nodes.remove_nodes("25")
# #show final nodes
# print(nodes.show_nodes())

# import sys
# sys.path.append('./')
# from nodes.node import Nodes


class LinkedList:
    def __init__(self):
        self.nd = Nodes()
        self.linkerlistchain = ""

    def add_val(self,val):
        # ll = self.nd.add_nodes_link(val)
        self.linkerlistchain = str(val) + "->" + self.linkerlistchain
        return self.show_ll()

    def show_ll(self):
        if self.linkerlistchain[-2:] == "->":
            rem = self.linkerlistchain[:-2]
            return rem

    def remove_ll(self,value:str) -> str:
        if self.linkerlistchain:
            self.linkerlistchain = self.linkerlistchain.replace(str(value) + "->","",1)
            return self.show_ll()
        else:
            return None



# ll = LinkedList()
# #add elements to linked list
# ll.add_val(10)
# ll.add_val(15)
# ll.add_val(20)
# ll.add_val(25)

# #remove elements in linked list
# ll.remove_ll(15)

# #show linked list
# print(ll.show_ll())

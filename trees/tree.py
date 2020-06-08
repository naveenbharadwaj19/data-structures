class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


#root
# root = TreeNode("Kris Jenner")
# child_1 = TreeNode("Kim Kardashian")
# child_2 = TreeNode("Kendall Jenner")
# child_3 = TreeNode("Kylie jenner")
# child_1_1 = TreeNode("North West")
# child_1_2 = TreeNode("Chicago West")
# child_3_1 = TreeNode("Stormi")
# #adding parent children
# root.add_child(child_1)
# root.add_child(child_2)
# root.add_child(child_3)
# child_1.add_child(child_1_1)
# child_1.add_child(child_1_2)
# child_3.add_child(child_3_1)


# #Traverse Tree
# print("___"*20)
# root.traverse()
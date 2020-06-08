class Heap:
    """Call either min or max not both at the same time """
    def __init__(self,array:list)-> list:
        self.array = array
        self.final_array = []

    def min_heap(self):
        while self.array:
            min_val = min(self.array)
            self.final_array.append(min_val)
            self.array.remove(min_val)
        return self.traverse_heap()

    def add_to_heap(self,value):
        print(f"Adding {value} to the heap")
        self.array.append(value)

    def max_heap(self):
        while self.array:
            max_val = max(self.array)
            self.final_array.append(max_val)
            self.array.remove(max_val)
        return self.traverse_heap()

    def remove_element(self,value):
        print(f"Removing {value} from the heap")
        self.final_array.remove(value)
        return

    def traverse_heap(self):
        return self.final_array


# h = Heap([1,3,6,9,5,8])
# #Add values
# # h.add_to_heap(5)
# # h.add_to_heap(11)
# # h.add_to_heap(17)


# #min or max
# h.min_heap()


# #Remove values
# # h.remove_element(17)
# # h.remove_element(5)
# # h.remove_element(11)

# #Traverse Heap
# print(h.traverse_heap())

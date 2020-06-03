import sys
sys.path.append("./")
from linked_list.linked_list import LinkedList

class Stack:
    def __init__(self,num):
        self.num = num
        self.ll = LinkedList()
        self.rooms = 0
        self.stack_val = []

    def push(self,val):
        if self.num !=self.rooms:
            self.ll.add_val(val)
            self.rooms += 1
            print(f"Adding {val} to the stacks")
            self.stack_val.append(val)
            return self.stack_val
        
        elif self.num ==self.rooms:
            print("No Space to add")
            
    def peek(self):
        try:
            return f"First element {self.ll.show_ll()[:2]}"
        except Exception:
            return "Nothing on stack"

    def pop(self):
        if self.rooms > 0:
            self.rooms -= 1
            print(f"Removing {self.stack_val[-1]} from the stack")
            self.stack_val.pop()

        else:
            print("Stack is empty")

# st = Stack(5)
# #push elements to stack
# st.push(10)
# st.push(20)
# st.push(30)
# st.push(40)
# st.push(50)
# st.push(60)

# #peek
# print("__"*10)
# print(st.peek())

# #pop 
# print("__"*10)
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.pop()
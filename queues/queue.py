import sys
sys.path.append("./")
from linked_list.linked_list import LinkedList

class Queue:
    def __init__(self,num):
        self.num = num
        self.ll = LinkedList()
        self.rooms = 0
        self.queue_val = []

    def add_to_queue(self,val):
        if self.num !=self.rooms:
            self.ll.add_val(val)
            self.rooms += 1
            print(f"Adding {val} to the queue")
            self.queue_val.append(val)
            return  self.queue_val
        
        elif self.num ==self.rooms:
            print("Queue is full")
            
    def view_queue(self):
        try:
            return f"First element in (FIFO) -> {self.queue_val[0]}"
        except Exception:
            return "Nothing in queue"

    def dequeue(self):
        if self.rooms > 0:
            self.rooms -= 1
            print(f"Removing { self.queue_val[0]} from the queue")
            self.queue_val.pop(0)

        else:
            print("Queue is empty")



# q = Queue(3)
# #add to queue
# q.add_to_queue(10)
# q.add_to_queue(20)
# q.add_to_queue(30)
# q.add_to_queue(40)

# #view queue
# print("__"*10)
# print(q.view_queue())

# # remove from queue
# print("__"*10)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
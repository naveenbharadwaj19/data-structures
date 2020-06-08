class HashMap:
  def __init__(self, array_size:int)-> int:
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key , count_collissions = 0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collissions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self,key,value):
    array_val = self.compressor(self.hash(key))
    check_val = self.array[array_val]
    if check_val is None:
      self.array[array_val] = [key,value]
    
    if check_val is not None:
      for i in range(self.array_size):
        try:
          check_array = array_val + i
          if self.array[check_array] is None:
            self.array[check_array] = [key,value]
            return
        except Exception:
          continue

  def retrieve(self,key):
    for items in self.array:
      if key in items:
        itr = iter(items)
        rtr_dict = dict(zip(itr,itr))
        return rtr_dict.get(key)



# hm = HashMap(11)
# #Assign 
# hm.assign("Mia","programmer")
# hm.assign("Zoe","Actress")
# hm.assign("Sue","Designer")
# hm.assign("Lou","Photographer")
# hm.assign("Rae","Professor")
# hm.assign("Tim","Financial advisor")
# hm.assign("Len","Painter")
# hm.assign("Moe","Writer")
# hm.assign("Bea","IT")
# hm.assign("Max","Artist")
# hm.assign("Tod","Server maintenance")
# print("__"*15)
# #Retrieve
# print(hm.retrieve("Sue"))
# print("__"*15)

# # Show the array
# # print(hm.array)
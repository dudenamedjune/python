class HashMap:
    capacity: int
    size: int   
    table: list
    def __init__(self):
        self.capacity = 11
        self.size = 0
        self.table = [None] * self.capacity
    
    def get_hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash += ord(key[i])
        return hash % self.capacity
    
    def locate_spot(self, key, index):
        if self.table[index] == None:
            return index
        else:
            return self.locate_spot(key, (index + 1) % self.capacity)

    def add_entry(self, key, value):
        index = self.get_hash(key)
        if self.table[index] == None:
            self.table[index] = [[key, value]]
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    print("Collision")
                    index = self.locate_spot(key, index)
                    self.table[index] = [[key, value]]
                    break
            else:
                self.table[index].append([key, value])
        self.size += 1
        if self.size > 0.75 * self.capacity:
            self.capacity *= 2
            self.rehash()

    def rehash(self):
        old_table = self.table
        self.table = [None] * self.capacity
        for i in range(len(old_table)):
            if old_table[i] != None:
                for j in range(len(old_table[i])):
                    self.add_entry(old_table[i][j][0], old_table[i][j][1])

    def get_value(self, key):
        index = self.get_hash(key)
        if self.table[index] == None:
            return None
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:            
                    return self.table[index][i][1]
            else:
                return None
        
    def set_value(self, key, value):
        index = self.get_hash(key)
        if self.table[index] == None:
            return False 
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i][1] = value
                    return True 
            else:
                return False 

    def delete_entry(self, key):
        index = self.get_hash(key)
        if self.table[index] == None:
            return None
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index].pop(i)
                    self.size -= 1
                    return True
            else:
                return False

    def get_size(self):
        return self.size
    
    def is_full(self):
        return self.size == self.capacity

    def __str__(self):
        string = ""
        for i in range(len(self.table)):
            if self.table[i] != None:
                for j in range(len(self.table[i])):
                    string += str(self.table[i][j][0]) + ": " + str(self.table[i][j][1]) + "\n"
        return string

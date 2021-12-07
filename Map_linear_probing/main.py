DEFAULT_INITIAL_CAPACITY = 4
DEFAULT_MAX_LOAD_FACTOR = 0.75 
MAXIMUM_CAPACITY = 2 ** 30 
class Map:
    def __init__(self, capacity = DEFAULT_INITIAL_CAPACITY, 
                 loadFactorThreshold = DEFAULT_MAX_LOAD_FACTOR):
        self.capacity = capacity
        self.loadFactorThreshold = loadFactorThreshold
        self.table = []
        for i in range(self.capacity):
            self.table.append([])
        self.size = 0 
    def put(self, key, value):
        if self.size >= self.capacity * self.loadFactorThreshold:          
            if self.capacity == MAXIMUM_CAPACITY:
                raise RuntimeError("Exceeding maximum capacity")
            self.rehash()
        bucketIndex = self.getHash(hash(key))
        self.table[bucketIndex].append([key, value])
        self.size += 1 
    def remove(self, key):
        bucketIndex = self.getHash(hash(key))
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for entry in bucket:
                if entry[0] == key:
                    bucket.remove(entry)
                    self.size -= 1 
                    break 
    def containsKey(self, key):
        bucketIndex = self.getHash(hash(key))
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for entry in bucket:
                if entry[0] == key:
                    return True
        return False        
    def containsValue(self, value):
        for i in range(self.capacity):
            if len(self.table[i]) > 0:
                bucket = self.table[i]
                for entry in bucket:
                    if entry[1] == value:
                        return True
        return False
    def items(self):
        entries = []
        for i in range(self.capacity):
            if self.table[i] != None:
                bucket = self.table[i]
                for entry in bucket:
                    entries.append(entry)
        return tuple(entries)
    def get(self, key):
        bucketIndex = self.getHash(hash(key))
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for entry in bucket:
                if entry[0] == key:
                    return entry[1]
        return None
    def getAll(self, key):
        values = []
        bucketIndex = self.getHash(hash(key))
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for entry in bucket:
                if entry[0] == key:
                    values.append(entry[1])
    
        return tuple(values)
    def keys(self):
        keys = []
        for i in range(0, self.capacity):
            if len(self.table[i]) > 0:
                bucket = self.table[i] 
                for entry in bucket:
                    keys.append(entry[0])
        return keys
    def values(self):
        values = []
        for i in range(self.capacity):
            if len(self.table[i]) > 0:
                bucket = self.table[i] 
                for entry in bucket:
                    values.append(entry[1])
        return values
    def clear(self):
        self.size = 0 
        self.table = [] 
        for i in range(self.capacity):
            self.table.append([])
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def rehash(self):
        temp = self.items() 
        self.capacity *= 2 
        self.table = [] 
        self.size = 0 
        for i in range(self.capacity):
            self.table.append([])
        for entry in temp:
            self.put(entry[0], entry[1]) 
    def toString(self):
        return str(self.items())
    def setLoadFactorThreshold(self, threshold):
        self.loadFactorThreshold = threshold
    def getTable(self):
        return str(self.table)
    def supplementalHash(self, h):
        h ^= (h >> 20) ^ (h >> 12)
        return h ^ (h >> 7) ^ (h >> 4)
    def getHash(self, hashCode):
        return self.supplementalHash(hashCode) & (self.capacity - 1)
def main():
    
    map = Map()
    map.put("Smith", 30) 
    map.put("Anderson", 31)
    map.put("Lewis", 29)
    map.put("Cook", 29)
    map.put("Cook", 129)
    
    print("Entry set in map: " + str(map.items()))
    print("The age for Lewis is " + str(map.get("Lewis")))
    print("Is Smith in the map? " + str(map.containsKey("Smith")))
    print("Is Johnson in the map? " + 
        str(map.containsKey("Johnson")))
    print("Is value 30 in the map? " + str(map.containsValue(30)))
    print("Is value 33 in the map? " + str(map.containsValue(33)))
    print("Is age 33 in the map? " + str(map.containsValue(33)))
    print("All values for Cook? " + str(map.getAll("Cook")))
    print("keys are " + str(map.keys()))
    print("values are " + str(map.values()))
    map.remove("Smith") 
    print("The map is " + map.getTable())
    map.clear()
    print("The map is " + map.getTable())

main()
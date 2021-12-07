class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element
    def addFirst(self, e):
        newNode = Node(e) 
        newNode.next = self.__head 
        self.__head = newNode 
        self.__size += 1 
        if self.__tail == None: 
            self.__tail = self.__head
    def addLast(self, e):
        newNode = Node(e) 
        if self.__tail == None:
            self.__head = self.__tail = newNode 
        else:
            self.__tail.next = newNode 
            self.__tail = self.__tail.next 
        self.__size += 1 
    def add(self, e):
        self.addLast(e)
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) 
        elif index >= self.__size:
            self.addLast(e) 
        else: 
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1
    def removeFirst(self):
        if self.__size == 0:
            return None 
        else:
            temp = self.__head 
            self.__head = self.__head.next 
            self.__size -= 1 
            if self.__head == None: 
                self.__tail = None 
            return temp.element 
    def removeLast(self):
        if self.__size == 0:
            return None 
        elif self.__size == 1: 
            temp = self.__head
            self.__head = self.__tail = None  
            self.__size = 0
            return temp.element
        else:
            current = self.__head
            for i in range(self.__size - 2):
                current = current.next
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None 
        elif index == 0:
            return self.removeFirst()  
        elif index == self.__size - 1:
            return self.removeLast() 
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element
    def isEmpty(self):
        return self.__size == 0
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " 
            else:
                result += "]" 

        return result

    def clear(self):
        self.__head = self.__tail = None

    def contains(self, e):
        return self.indexOf(e) >= 0
    def remove(self, e):
        index = self.indexOf(e)
        if index == -1:
            return False
        else:
            self.removeAt(index)
            
        return True
    def indexOf(self, e):
        current = self.__head 
        i = 0
        while current != None:
            if current.element == e:
                return i
            i += 1
            current = current.next
        return -1
    def set(self, index, e):
       self.removeAt(index)
       self.insert(index, e) 
    def __getitem__(self, index):
        return self.get(index)
    def __iter__(self):
        return LinkedListIterator(self.__head)
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None
class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    
class MyLinkedList(LinkedList):
    def remove(self, item):
        index = self.indexOf(item)
        self.removeAt(index)
    def set(self, index, e):
       self.removeAt(index)
       self.insert(index, e)  
def main():
    lista = input("Enter list1: ").split()
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    
    print("list1.indexOf('red') is", list1.indexOf('red'))
    list1.remove("red")
    print("after invoking list1.remove('red'), list1 is", list1)
    index = int(input("Enter an index: "))
    list1.set(index, "orange")
    print("after invoking list1.set('" + str(index) + " , orange)", 
        "list1 is", list1)
main()
        
        
    
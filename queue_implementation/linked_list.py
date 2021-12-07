'''
Singly Linked list class, Node class, Linked List Iterator class

'''

class Node:
    ''' Node class contains one data field and one pointer '''
    def __init__(self, e):
        self.element = e
        self.next = None # Point to the next node, default None

class LinkedList:
    ''' LinkedList class provides a linked struture to store data '''
    def __init__(self):
        '''construtor to create a LinkedList instance'''
        self.__head = None
        self.__tail = None
        self.__size = 0
    def get_first(self):
        ''' return the first element '''
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    def get_last(self):
        ''' return the last element '''
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    def add_first(self, e):
        ''' add node at the first position '''
        new_node = Node(e) # Create a new node
        new_node.next = self.__head # link the new node with the head
        self.__head = new_node # head points to the new node
        self.__size += 1 # Increase list size
        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head
    def add_last(self, e):
        ''' add node at the last position '''
        new_node = Node(e)
        if self.__tail == None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = self.__tail.next
        self.__size += 1
    def add(self,e):
        ''' add node at the last position '''
        self.add_last(e)
        
    def insert(self, index, e):
        ''' insert a new node at a specified location '''
        if index == 0:
            self.add_first(e)
        elif index >= self.__size:
            self.add_last(e)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1
    def remove_first(self):
        ''' remove first node '''
        if self.__size == 0:
            return None
        else:
            temp = self.__head
            self.__head = self.__head.next
            self.__size -= 1
            if self.__head == None:
                self.__tail = None
            return temp.element
    def remove_last(self):
        ''' remove last node '''
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
    def remove_at(self, index):
        ''' remove node at a specified location '''
        if index < 0 or index >= self.__size:
            return None
        elif index == 0:
            return self.remove_first()
        elif index == self.__size - 1:
            return self.remove_last()
        else:
            previous = self.__head
            for i in range(1, index):
                previous = previous.next
            current = previous.next
            previous.next = current.next
            self.__size -=1
            return current.element
    def is_empty(self):
        ''' check if linkedlist is empty '''
        return self.__size == 0
    def get_size(self):
        ''' return the size of linked list '''
        return self.__size
    def __str__(self):
        ''' override method to display self '''
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += " -> " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result
    def clear(self):
        ''' clear the linkedlist '''
        self.__head = self.__tail = None
        self.__size = 0
    def contains(self, e):
        ''' return true if list contains e '''
        return self.index_of(e) >= 0
    def index_of(self, e):
        ''' return the position of e, return -1 if e does exist '''
        current = self.__head 
        index = 0
        while current != None:
            if current.element == e:
                return index
            index += 1
            current = current.next
        return -1
    def __iter__(self):
        '''return an iterator for the linked list '''
        return LinkedListIterator(self.__head)

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
   
        
    
        
    

''' Queue class
    Queue is a classical data structure which use FIFO (first in first out) method
        to add and remove data. It is to add/remove person from a waiting line.
        You insert item at the end of the queue and remove item from the beginning of the queue.
        enqueue() method allows you to insert item at the end of the queue.
        dequeue() method allows you to remove item from the beginning of the queue.
        To implement queue in Python, we can use built-in list structure, or use a linked
        structure. Using Python list, you can use the method to append() to enqueue and
        pop(0) to dequeue. Based on the performance, the linked structure will be a
        better choice to implement the Queue.

'''
from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.__elements = LinkedList()

    # Adds an element to this queue
    def enqueue(self, e):
        self.__elements.add(e)
    
    # Removes an element from this queue
    def dequeue(self):
        if self.get_size() == 0:
            return None
        else:
            return self.__elements.remove_at(0)
    
    # Return the size of the queue
    def get_size(self):
        return self.__elements.get_size()
    
    # Returns a string representation of the queue
    def __str__(self):
        return self.__elements.__str__()

    # Return true if queue is empty 
    def is_empty(self):
        return self.get_size() == 0

# end of Queue class





















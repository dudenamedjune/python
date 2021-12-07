import grocery_queue
import random

class GroceryStore:
    def __init__(self, length_simulation, average_customer_time, probability_new_arrival):
        self.__length_simulation = length_simulation
        self.__average_customer_time = average_customer_time
        self.__probability_new_arrival = probability_new_arrival
        self.__cashier = Cashier(self.__length_simulation, 0, Customer.generate_customer(self.__probability_new_arrival, 0, self.__average_customer_time))
        return

    def run_simulation(self):
        for current_time in range(0, self.__length_simulation):
            new_customer = Customer.generate_customer(self.__probability_new_arrival, current_time, self.__average_customer_time)
            if new_customer:
                self.__cashier.add_customer(new_customer)
            self.__cashier.serve_customer(current_time)

    def __str__(self):
        return self.__cashier.__str__()
    
class Cashier:
    def __init__(self, total_customer_wait_time, customer_served, current_customer):
        self.__total_customer_wait_time = total_customer_wait_time
        self.__customer_served = customer_served
        self.__current_customer = current_customer
        self.__queue = grocery_queue.Queue()
        return
    def add_customer(self, cust):
        self.__queue.enqueue(cust)
        return
    def serve_customer(self, current_time):
        if self.__current_customer is None:
            if self.__queue.is_empty():
                return
            else:
                self.__current_customer = self.__queue.dequeue()
                self.__total_customer_wait_time += current_time - self.__current_customer.get_arrival_time()
                self.__customer_served += 1
                self.__current_customer.serve()
                if self.__current_customer.get_amount_of_service_needed() == 0:
                    self.__current_customer = None
        return

    def __str__(self):
        return "Total customers served: " + str(self.__customer_served) + "\nTotal customers still waiting in the queue: " + str(self.__queue.get_size()) + "\nAverage customer wait time: " + str(self.__total_customer_wait_time/self.__customer_served) 

class Customer:
    def __init__(self, arrival_time, amount_of_service_needed):
        self.__arrival_time = arrival_time
        self.__amount_of_service_needed = amount_of_service_needed
        return

    @classmethod 
    def generate_customer(cls, probability_of_new_arrival, arrival_time, average_time_per_customer):
        if probability_of_new_arrival >= random.random():
            return Customer(arrival_time, average_time_per_customer)
        else:
            return None
    
    def get_arrival_time(self):
        return self.__arrival_time

    def get_amount_of_service_needed(self):
        return self.__amount_of_service_needed
    
    def serve(self):
        self.__amount_of_service_needed -= 1
        return
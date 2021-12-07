import grocery_store

def main():
    running_time = input("Enter the total running time: ")

    average_time_per_customer = input("Enter the average time per customer: ")

    probability_of_arrival = input("Enter the probability of a new arrival: ")

    store = grocery_store.GroceryStore(int(running_time), int(average_time_per_customer), float(probability_of_arrival))
    store.run_simulation()

    print(store)
    
main()
import HashMap

def main():
    hash_map = HashMap.HashMap()
    # bonus capacity rehash implemented but does the test data in the assignment instructions doesn't test that case as it is smaller than the default capacity 
    test_list = [("Printer",20) ,("Notebook",30),("Pen",100),("Scanner",25),("Toner",50),("Paper",200),("Pencils",150)]
    for (key, value) in test_list:
        hash_map.add_entry(key, value)
        print(f"value of {key} is {hash_map.get_value(key)}")    
        print("updating value for key: " + key)
        hash_map.set_value(key, value + 10)
        print(f"value of {key} should now be {value + 10}: get_value {hash_map.get_value(key)} \n")
    print(hash_map)

    hash_map.delete_entry("Pen")
    print("hash map should not include pen anymore: ")
    print(hash_map)
main()
def check_order(a_list):
    if a_list == sorted(a_list, reverse=True):
        return "descending order"
    elif a_list == sorted(a_list):
        return "ascending order"
    else:
        return "no order"

def main():
    list = [1,2,3,4,5,6,7,8,9,10]
    print(check_order(list))

main()
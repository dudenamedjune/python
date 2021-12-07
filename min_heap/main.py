def min_heapify(array, i):
    left = 2*i+1
    right = 2*i+2
    smallest = i
    if left < len(array) and array[left] < array[i]:
        smallest = left
    if right < len(array) and array[right] < array[smallest]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        return min_heapify(array, smallest)

def main():
    string = input("Enter numbers:")
    array = string.split()
    int_array = [float(i) for i in array]
    int_array.sort()
    for i in range(len(int_array)//2 + 1, -1, -1):
        min_heapify(int_array, i)
    print(' '.join(str(s) for s in int_array))
main()
# (Pattern matching)

# Write a program that prompts the user to enter two strings and tests whether the second string is a substring in the first string. Suppose the neighboring characters in the string are distinct. (Don’t use the find method in the str class.) Analyze the time complexity of your algorithm. Your algorithm needs to be at least O(n) time.

# Sample Run

# Enter a string s1: Welcome to Python

# Enter a string s2: come

# matched at index 3

def match(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i+len(s2)] == s2:
            return i
    return -1

def main():
    s1 = input("Enter a string s1: ")
    s2 = input("Enter a string s2: ")
    matched_index = match(s1, s2)
    if matched_index > -1:
        print("matched at index", matched_index)
    
    
main()
def main():
    text = input("enter text: ")
    words = set(text.split(" "))
    print(" ".join(sorted(words)))
main()
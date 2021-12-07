def count_vowels_and_consonants(s):
    vowels = set() 
    consonants = set()
    for c in s:
        if c in "aeiouAEIOU":
            vowels.add(c)
        elif c.isalpha():
            consonants.add(c)
    return len(vowels), len(consonants)

def main():
    text = input("Enter a string:")
    (vowels, consonants) = count_vowels_and_consonants(text)
    print(f"The number of vowels is {vowels}")
    print(f"The number of consonants is {consonants}")

main()
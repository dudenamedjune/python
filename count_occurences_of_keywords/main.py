keywords = {
    'and': 0, 
    'as': 0,
    'assert': 0, 
    'break': 0, 
    'class': 0, 
    'continue': 0, 
    'def': 0, 
    'del': 0, 
    'elif': 0, 
    'else': 0, 
    'except': 0, 
    'finally': 0, 
    'for': 0, 
    'from': 0, 
    'global': 0, 
    'if': 0, 
    'import': 0, 
    'in': 0, 
    'is': 0, 
    'lambda': 0, 
    'nonlocal': 0, 
    'not': 0, 
    'or': 0, 
    'pass': 0, 
    'raise': 0, 
    'return': 0, 
    'try': 0, 
    'while': 0, 
    'with': 0, 
    'yield': 0
}
input = input("Enter Python source code: ")
for word in input.split():
    if word in keywords:
        keywords[word] += 1
for keyword, count in keywords.items():
    if count > 0:
        print(f"{keyword}: {count}")
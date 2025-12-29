from collections import Counter
s = input()
c = Counter(s)
found = False
found_char = ""
p = ""
for char in c:
    if c[char] % 2 == 1:
        if found:
            print("NO SOLUTION")
            exit()
        found = True
        found_char = char
    p += char * (c[char] // 2)

print(p + found_char + p[::-1])

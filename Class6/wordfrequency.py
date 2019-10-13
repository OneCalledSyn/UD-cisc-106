from collections import Counter

word = input("What word should we analyze? ").upper()

counts=Counter(word) # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})

for i in word:
    print(i,counts[i])
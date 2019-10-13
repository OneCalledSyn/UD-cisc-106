s = "Taylor is a power lifter"

s = s.split(" ")

print (s)

for i in range(0,5):
    s[i] = sorted(s[i])

print (s)

s = ''.join(str(s))

print (s)

#Easy code by Andy

def word_sort(sentence):
    return " ".join(map(lambda x: "".join(sorted(x)), sentence.split()))

print(word_sort("Andy is the greatest"))
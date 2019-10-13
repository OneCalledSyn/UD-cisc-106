L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def bundle(L, size):
    """
bundle consumes a list, L, of individual characters
it produces a list of strings of length size containing the characters from L
the final string is the remaining characters
    """
    if len(L) < size:
        return ["".join(L)]
    #Your code here
    else:
        return ["".join(L[0:3])]
        

print (L)

assert bundle(["a","b","c","d","e"], 3) == ["abc", "de"]
assert bundle(["a","b","c","d","e"], 2) == ["ab", "cd", "e"]
assert bundle(["a","b"], 5) == ["ab"]
print("All tests passed")
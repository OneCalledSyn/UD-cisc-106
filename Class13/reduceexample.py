from functools import reduce

def sum(a, b):
    return a + b

print(reduce(sum, range(10), 0))

def int2str(ans_so_far, new_int):
    if new_int % 2 == 0:
        return ans_so_far + "E"
    else:
        return ans_so_far + "O"

print(reduce(int2str, range(10), "EO pattern is: "))
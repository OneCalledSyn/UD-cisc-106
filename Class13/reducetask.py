from functools import reduce

def sum(a, b):
    return a + b

print(reduce(sum, range(2, 70, 5), 2))

def int2str(ans_so_far, new_int):
    if new_int % 3 == 0:
        return ans_so_far + "D"
    else:
        return ans_so_far + " "

print(reduce(int2str, range(10), "Divisble by 3 pattern is: "))
def integers():
    i = 0
    while True:
        yield i
        i += 1

int_iter = integers()

print(next(int_iter))
print(next(int_iter))
print(next(int_iter))  
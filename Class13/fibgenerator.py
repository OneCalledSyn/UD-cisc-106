def fibgen():
    a = 0
    b = 1
    while True :
        yield a
        a, b = b, a + b

fibber = fibgen()

for n in fibber :
    if n > 60 :
        break
    else :
        print (n)
f = open('haiku.txt', 'w')
f.write("Python code is fun \n I do not understand though \n someone please help me")
f.close()

f = open('haiku.txt')
for line in f:
    print(line)
f.close()    
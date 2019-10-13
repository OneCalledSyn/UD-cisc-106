f = open('filelooper.txt', 'w')
f.write("Hi there. \n\
I am a competer. \n\
Are you a human or a computer?")
f.close()

f = open('filelooper.txt')
temp = 'start'
while temp != '':
    temp = f.read(3)
    print(temp)
    print("\n**\n")
f.close()    

#seek(0) ---> sets the file's current position at the offset

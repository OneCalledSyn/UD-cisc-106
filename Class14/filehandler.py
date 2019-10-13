f = open('filehandler.txt', 'w')
f.write("Hi there. \nI am a computer. \nAre you a human or a computer?")
f.close()

f = open('filehandler.txt')
lngstr = f.read()

print (len(lngstr), " characters in that file\n")

lngstr2 = f.read()
print(len(lngstr2), " characters in second reading")
#f.read() will return an empty string if at the end of the file, so the second reading with have 0 length
#f.read(n) will read n characters in the file

f.close()
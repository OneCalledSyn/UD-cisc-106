def functionA(input):
    input += " o-rama"

def functionB(input):
    input += [2, 3, 1]

def functionC(input):
    input["+="] += "+="

def functionD(input):
    input += 231


inputA = "Bill" #str
inputB = ["Bill"] #list
inputC = {"+=":"Bill"} #dict
inputD = ord("B")+ord("i")+ord("l")+ord("l") #int

print(functionA(inputA))
print(functionB(inputB))
print(functionC(inputC))
print(functionD(inputD))
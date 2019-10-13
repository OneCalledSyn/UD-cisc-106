#Practice Test
#Problem 1:
x = True
y = False
z = True
w = z and not x or not y

#What value is assigned to w? True

#Problem 2:
def f(y):
    return y+4

assert f( f( f( f(1)))) == -----
#what value goes at -----? 17

#Problem 3:
banana = "dole"
fruit = "banana"
fruit = banana
banana = fruit
print(banana, fruit)
#What gets displayed? dole dole

#Problem 4:
total = 0
for value in [3, 5, 2, 7]:
    total = total + value + 3
    print(total)
#What will be printed to the screen? 6 14 19 29

#Problem 5:
total = 0
for i in range(4, 80, 4):
    total = i
print(i)
#What will be displayed? 76

#Problem 6:
def fork(a, b):
    if (a > b):
        a = a + b
    else:
        a = a - b
output = fork(10, 12)
print(output)
#What will be displayed? Nothing, a=-2 and b=12

#Problem 7:
for a in [3, 6, 1, 2]:
    for b in range(1, 3):
        print(a,b)
#What will be displayed? (3,1)(3,2)(6,1)(6,2)(1,1)(1,2)(2,1)(2,2)

#Problem 8:
g = 77
if x <= 100:
    grade = "A"
elif x < 90:
    grade = "B"
elif x < 80:
    grade = "C"
else:
    grade = "D"
print(grade)
#What will be displayed? A

#Problem 9:
for a in range(3):
    for b in range(4):
        print(a, b)
#What will be displayed? Fuck off

#Problem 10:
#Write code which computes and prints the product:
# 2 * 5 * 8 * 11 * 14 * ... * 905

total = 2
for a in range (5,906,3)
    total = total*a
print(total)    


#Problem 11:
# Write a function which takes in non-negative p
# and prints "*5" if p is a positive multiple of 5
# prints "not *5" if p is positive but not a positive multiple of 5
# and prints "ZERO" if p is 0.

def root_five (n):
    if n == 0:
        print("ZERO")
    elif n % 5:
        print("*5")
    else:
        print("not *5")

#Problem 12:
#Write a function which computes the average of the first n positive numbers

def meanpos (n):
    total = 0
  for i in range(1, n+1):
    total += i
  return total / n
n= int(input("How many students are in the class?: "))

grade_book = {}

for i in range(n):
    raw_line = input("Student name: ")
    S = raw_line.split()
    student_name = S[0]
    grades = list(map(float, S[1:]))
    grade_book[student_name] = grades
    
lookup_name = input("What student should we look up?: ")
print( "{0:.2f}".format(sum(grade_book[lookup_name]) / len(grade_book[lookup_name]))) 
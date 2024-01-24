"""
number in python
int ,float ,complex

import math
------>STRINGS 
a: int = 3
b: float = 3.0191
c: complex = complex(1, 3)
print(type(a), type(b), type(c))
name = "learning programming "

----->SPLITTING 
name = input("Enter your name :\n")
splitted_text = name.split(" ")
print(f"first  Nmae is {splitted_text[0]}")
print(f"second  Nmae is {splitted_text[1]}")
print(f"third  Nmae is {splitted_text[2]}")
print(len(name))


# LIST IN PYTHON
# --->


students = ["Ram", "Shyam", "Hari", "myself"]
roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

count_of_students = len(students)
roll_count = roll.__len__()

print(count_of_students, roll_count)


for x in range(100):
    print(x, "python is very intersesting😂😂")

roll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in roll:
    print(i)
i = 0
while(i<=5):
    print(i)
    i += 1
students = []

 last task 
--->  wap in such a way that
       *when user enters input 'ram' as a name
       *break loop and print the list 
       *otherwise keep on appending items to list
       *and ask for next input from terminal 

"""
name = []
i = 0
while name[-1] != "ram" if name.__len__() > 0 else True:
    name1 = input("enter your name:\n")
    name.append(name1)
print(name)

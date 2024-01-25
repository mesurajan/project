# py_functions
# functions in python
# arguments in function
# return to function

"""
def name_printer():
    print("My name is surajan shrestha")



#args no return type
    def name_printer(name):
        print(f"My name is {name}")

#single args no  singe return 
        """

"""
def calculate_sum(a=0, b=0):
    return a + b


total_sum = calculate_sum(1, b=2)
print(total_sum)

"""
"""

def display(*args, **surajan):
    head = surajan.get("Last_words")
    print(head)
    tail = args.get("Don")
    print(tail)
    # print(args,surajan)


print(display("MY ", "name", Don="Sanchita"))
print(display("MY ", "name", Last_words="shrestha"))

"""
"""
wap in python to find the sum of all numbers in a list using function .
create a function in such that it accepts kwargs as a list of numbers,
calculate the sum,return the sum and print it .

result = [1, 2, 3, 4, 5, 6, 7]


def add(*surajan, **kwargs):
    return sum([*list(surajan), *kwargs.get("num")])


result1 = add(1, 2, 3, 4, 5, 6, 7, 8, 9, num=result)
print(f"the sum is :{result1}")


wap to merge two dict pass a dict obj in args and then a no of kyewors arguments.merge those two 
dictionaries and return it ,print it 
"""


def surajan(*args, **kwargs):
    return {**args[0], **kwargs}


dict1 = {"name": "Milan", "age": "35"}
dict2 = {"name": "Avay", "age": "67"}
merged_dict = surajan(dict1, data=dict2)
print(f"The merged data is :{merged_dict}")

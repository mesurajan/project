# recursion function in python

# calculating the factorial of x where x>=1


def factorial_function(x):

    if not isinstance(x, int):  # isinstance =>
        return "Illegal value provided"

    if x < 1:
        return "Value cannot be less than 1"
    if x == 1:
        return 1
    else:
        print(f"Value in this iteration is :{x}*{x-1}")
        return x * factorial_function(x - 1)


# ret1 = factorial_function("abc")
# ret2 = factorial_function(0)
# ret3 = factorial_function(-1)
ret4 = factorial_function(5)


# print(f"first call returned :{ret1}")
# print(f"second call returned :{ret2}")
# print(f"Third call returned :{ret3}")
print(f"Last call returned :{ret4}")


"""
how recursion works in this function :

Factorial_function(5)
5* factorial_function(4)
5*4 factorial_function(3)
5*4*3 factorial_function(2)
5**4*3*2 factorial_function(1)
5**4*3*2*1 
when it reaches to base case (i.e., when x==1), it starts 
returning values backward and multiplying them by each other until
it reachs the first calling point i.

"""

# use of lambda function

# y = lambda x: x + 3

# def y(x):
# return x+3    ----mathi ko line 3 equivalent ti line 5 and 6


fact = lambda n: n * fact(n - 1) if n > 1 else 1
print(fact(5))






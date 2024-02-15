# exception handeling

from math import factorial


try:
    print("Trying to execute value")
    ret = factorial(5)
    print(f"The factorial is :{ret}")


except Exception as e:
    print("exception occured")
    print(f"Exception details :\n {e.args}")

finally:
    print("function execution  complete ")

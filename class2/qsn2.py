""""
Wap to get name ,age ,religion,father_name,mother_name,college_name,
as inputs from terminal.Declare an empty dict .Add key value pairs to a directory and 
print results.

"""
file = ["name", "age", "religion", "father_name", "mother_name", "college_name"]
user_details = {}
for detail in file:
    user_details.setdefault(detail, input(f"Enter your {detail}\n"))
print(user_details)
"""
for detail in user_details:
    print(detail)
print([detail for detail in user_details])

"""
breakpoint()

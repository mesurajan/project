# used for filtering items in list to return a new list


students = [
    {"Name": "Ram", "Age": 20},
    {"Name": "Ravana", "Age": 30},
    {"Name": "sita", "Age": 23},
    {"Name": "Laxman", "Age": 29},
    {"Name": "Nakul", "Age": 40},
]
fv = filter(lambda y: "R" in y["Name"], students)
print(fv)
fv = list(fv)
print(fv)

"""







"""

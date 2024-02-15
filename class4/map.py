# Map means transforms

students = [{"Name": "John", "Age": 15}, {"Name": "Jane", "Age": 12}]
# We can use map to apply a function on each element of the list.
mapped = list(map(lambda student: (student["Age"]), students))
print(mapped)

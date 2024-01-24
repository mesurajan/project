user = {"name": "surajan", "age": "18", "address": "New jersey", "country": "nepal"}

print("Full name is ", user.get("name", "No Name"))
# getting values of dict
print(user.keys())
print(user.values())
user.setdefault("fathers_name", "Rudra prashad shrestha")
user["goal"] = "Greatest of all"
user.get("name")
user.get("mother_name", "Default value if no key present")

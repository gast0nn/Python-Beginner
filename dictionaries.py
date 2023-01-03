user_dictionary = {
    'username': 'aevian',
    'name': 'gaston',
    'age': '23'
}
user_dictionary["married"] = True
print(user_dictionary)

print(user_dictionary.get("username"))

for x, y in user_dictionary.items():
    print(x, y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary)


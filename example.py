person = {}

while True:
    name = input('name: ')
    age = int(input('age: '))
    person[name] = age
    another = input('add more? y/n')
    if another == 'y':
        continue
    else:
        break
ages = list(person.values())
for age in set(ages):
    count = ages.count(age)
    print(f"{age} years old - {count}")
# for (key,value) in person.items():
#     print(f"{key} is {value} years old")
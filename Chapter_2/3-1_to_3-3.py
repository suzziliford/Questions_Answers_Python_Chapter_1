motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles [0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print(first_owned)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print("\nA" + too_expensive.title() +" is too expensice for me.")

dinner_list = ['buddah', 'louis_cole', 'John_Coltrane']
print(dinner_list)

message = ("dear " + dinner_list[0].title() + "Please come to my dinner party. I love you, Matty")
print(message)

dinner_list.insert(2, 'Tilla')

print(dinner_list)

dinner_list.append('jesus')
print(dinner_list)

dinner_list.insert(2, 'cleopatra')
print(dinner_list)

dinner_list.sort()
print(dinner_list)

dinner_list.sort(reverse=True)
print(dinner_list)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

message=("yay")
print(message)

cars.reverse()
print(cars)

len(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(cars)
len(cars)

places = ['japan', 'italy', 'amsterdam', 'brasil', 'india']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.reverse()

len(places)
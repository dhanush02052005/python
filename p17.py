names = ['Snowball', 'Chewy', 'Bubbles','Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat'] 
age = [1, 2, 2, 6]

for i in range(len(names)):
    print(f"{names[i]} the {animal[i]} is {age[i]}")

for  names,animal,age in zip(names,animal,age):
    print(f"{names} the {animal} is {age}")
    
# --------------
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class=class_1+class_2
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)


# --------------
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
math = courses['Math']
english = courses['English']
history = courses['History']
french = courses['French']
science = courses['Science']
total = math + english + history + french + science
print (total)

# Insert percentage formula
percentage = (total * 100 / 500)

# Print the percentage
print(percentage)
# Code ends here


# --------------
mathematics={'Geoffrey Hinton': 78,'Andrew Ng': 95,'Sebastian Raschka': 65,'Yoshua Benjio': 50, 'Hilary Mason': 70,'Corinna Cortes': 66, 'Peter Warden': 75}
print(mathematics['Geoffrey Hinton'])
print(mathematics['Andrew Ng'])
print(mathematics['Sebastian Raschka'])
print(mathematics['Yoshua Benjio'])
print(mathematics['Hilary Mason'])
print(mathematics['Corinna Cortes'])
print(mathematics['Peter Warden'])
topper = max(mathematics,key = mathematics.get)
print (topper)



# --------------
# Given string
topper = 'andrew ng'
first_name=(topper.split()[0])
print(first_name)
last_name=(topper.split()[1])
print(last_name)
full_name=last_name + ' ' + first_name
print(full_name)
print(full_name.upper())
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here



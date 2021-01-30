print('Only two guests can be invited to dinner.')

while len(persons)>2:
    	print(persons.pop() + ", I can't invite you to have dinner with me.")

for person in persons:
	print(person + ', you are still in my list.')

del persons[0]
del persons[0]

print(persons)
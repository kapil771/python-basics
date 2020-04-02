class Person(object):
	def __init__(self,name):
		self.name = name;
		self.__education = 'Engineering'	# Private Variable


	def displayInfo(self):
		name = self.name
		education = self.__education
		print('My name is', name, 'and I have completed my', education)

person = Person('Omkar')
person.displayInfo()
print(person.name)                           # Can be accessed as it is public variable
#print(person.__education)                  # Throws an error
print(person._Person__education)
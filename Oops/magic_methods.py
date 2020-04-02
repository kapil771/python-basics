class Employee(object):
	def __init__(self, firstname, lastname, salary = 0):
		self.firstname = firstname
		self.lastname = lastname
		self.salary = salary


	def __str__(self):
		return 'Full Name: ' + self.firstname + ' ' + self.lastname

	# Implements behaviour for built in type comparison to int
	def __int__(self):
		return self.salary

	def __add__(self, other):
		return self.salary+other.salary

	def __mul__(self, other):
		return self.salary*other.salary

	def __eq__(self, other):
		return self.salary==other.salary


Omkar = Employee('Omkar', 'Pathak', 1000)
Jagdish = Employee('Jagdish','Pathak', 2000)
print(Omkar)
print(Jagdish)
print(int(Omkar))
print(int(Jagdish))
print(Omkar + Jagdish)      # 3000 (This output because of __add__ method overloading)
print(Omkar * Jagdish)      # 2000000 (__mul__)
print(Omkar == Jagdish)
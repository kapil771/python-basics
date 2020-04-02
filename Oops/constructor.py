class Vehicle():
	def __init__(self):
		print('Calling init')
		self.val = 0
		self.cost = 10000


	def incrementVehicle(self):
		self.val += 1

vehicleObj = Vehicle();
print(vehicleObj.val)

vehicleObj.incrementVehicle()
vehicleObj.incrementVehicle()
print('First obj value after incrementing:',vehicleObj.val)      #2

bike = Vehicle()       #__init__ is called makes val 0 for this ANOTHER instance
print('Second obj value:',bike.val)
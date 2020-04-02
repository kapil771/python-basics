class Data(object):
	def getData(self):
		print('In data!')


class Time(Data):
	def getTime(self):
		print('In Time!')


if __name__ == '__main__':
	data = Data()
	time = Time()

	data.getData()
	time.getTime()
	time.getData()
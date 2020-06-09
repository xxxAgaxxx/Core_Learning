class MutableInteger:
	def __init__(self, value):
		if (isinstance(value, int)):
			self.__value = value
		else:
			self.__value = value.__value

	def add(self, value=1):
		self.__value += value

	def sub(self, value=1):
		self.__value -= value

	def get(self):
		return self.__value

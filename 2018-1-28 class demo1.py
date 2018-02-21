class Foo:
	x = 7 #定义一个类变量
	def __init__(self,number):  #定义初始化方法
		self.x = number   
		return None
	def show_X(self):
		print('In Foo\'s show_X menthod')
		print(self.x)
		return None
	@staticmethod			
	def set_X(number):
		Foo.x = number
		return None
	@classmethod
	
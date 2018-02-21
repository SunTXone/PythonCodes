Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def shell_1(fun):
	def wrap():
		print('Start')
		print(fun)
		print('End')
	return wrap

>>> @shell_1
def bar():
	print('I am in bar.')

	
>>> bar()
Start
<function bar at 0x017E2540>
End
>>> def shell_1(fun):
	def wrap():
		print('Start in shell_1-wrap.')
		fun()
		print('End in shell_1-wrap.')
	return wrap

>>> bar()
Start
<function bar at 0x017E2540>
End
>>> @shell_1
def bar():
	print('I am in bar.')

	
>>> bar()
Start in shell_1-wrap.
I am in bar.
End in shell_1-wrap.
>>> 

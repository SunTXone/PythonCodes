Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def shell_1(fun):
	def wrap():
		print('Start shell_1-wrap')
		fun()
		print('End shell_1-wrap')
		print(fun.__name__)

		
>>> @shell_1
def bar():
	print('This is decorate_function:bar.')

	
>>> bar
>>> f = shell_1(bar)
>>> f()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    f()
TypeError: 'NoneType' object is not callable
>>> f.__name__
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f.__name__
AttributeError: 'NoneType' object has no attribute '__name__'
>>> type(f)
<class 'NoneType'>
>>> del f
>>> del bar
>>> del shell_1
>>> def shell_1():
	def wrap():
		print('This is a decorate demo.')
	return wrap

>>> @shell_1
def bar():
	print('This is outer funciton')

	
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    @shell_1
TypeError: shell_1() takes 0 positional arguments but 1 was given
>>> del shell_1
>>> del bar
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del bar
NameError: name 'bar' is not defined
>>> def shell_1(fun):
	def wrap():
		print('Start')
		print(fun)
		print('End')
	return wrap

>>> @shell_1
def bar():
	print('Demo in funciton:bar.')

	
>>> bar
<function shell_1.<locals>.wrap at 0x02324DF8>
>>> del bar
>>> del shell_1
>>> def shell_1(fun):
	def wrap():
		print('Start in shell_1-wrap.')
		fun()
		print('End in shell_1-wrap.')
	return wrap

>>> @shell_1
def bar():
	print('Demo in bar.')
	print(__name__)

	
>>> bar
<function shell_1.<locals>.wrap at 0x02324E88>
>>> 
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bar', 'shell_1']
>>> del bar
>>> del shell_1
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> 

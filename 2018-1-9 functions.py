Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #传递函数
>>> def ba():
	print('I am in bar()')

	
>>> def foo(func):
	func()

	
>>> foo(ba)
I am in bar()
>>> def power_seq(func,seq):
	return [func(i) for i in seq]

>>> def pingfang(x):
	return x**2

>>> __name__
'__main__'
>>> if __name== "__main__":
	num_seq = [111,3.14,2.91]
	r = power_seq[pingfang,num_seq]
	print(num_seq)
	print(r)

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    if __name== "__main__":
NameError: name '__name' is not defined
>>> 
KeyboardInterrupt
>>> if __name__ == "__main__":
	num_seq = [111,3.14,2.91]
	r = power_seq[pingfang,num_seq]
	print(num_seq)
	print(r)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    r = power_seq[pingfang,num_seq]
TypeError: 'function' object is not subscriptable
>>> if __name__ == "__main__":
	num_seq = [111,3.14,2.91]
	r = power_seq(pingfang,num_seq)
	print(num_seq)
	print(r)

	
[111, 3.14, 2.91]
[12321, 9.8596, 8.468100000000002]
>>> pingfang(i) for i in num_seq
SyntaxError: invalid syntax
>>> [pingfang(i) for i in num_seq]
[12321, 9.8596, 8.468100000000002]
>>> (pingfang(i) for i in num_seq)
<generator object <genexpr> at 0x0251D930>
>>> 

>>> #嵌套函数
>>> def foo():
	def bar():
		print("bar() is running")
	print("foo() is running")

	
>>> foo()
foo() is running
>>> #上例在foo函数中定义了bar函数，在foo函数中没有调用bar函数，所有没执行bar函数的输出
>>> 
>>> #新例子，在函数中定义函数，并调用
>>> def foo():
	def far():
		print("bar() is running")
	bar()     # 在foo函数的定义中显式执行bar函数
	print('foo() is running')

	
>>> foo()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    foo()
  File "<pyshell#52>", line 4, in foo
    bar()     # 在foo函数的定义中显式执行bar函数
NameError: name 'bar' is not defined
>>> #嵌套函数的名字写错误，重试
>>> def foo():
	def bar():
		print("bar() is running")
	bar()     # 在foo函数的定义中显式执行bar函数
	print('foo() is running')

	
>>> foo()
bar() is running
foo() is running
>>> #嵌套函数定义、演示成功
>>> #注意：函数内嵌套定义的函数，不能在定义函数外部单独调用。如在主函数外调用主函数的嵌套函数，显示“NameError”
>>> 
>>> #为方便描述，将有嵌套函数的函数成为“主函数”或“定义函数”，主函数内定义的嵌套函数称为“嵌套函数”
>>> '''嵌套函数中的变量与主函数的变量关系、作用范围和函数中的变量与全局变量的关系、作用范围类似 '''
'嵌套函数中的变量与主函数的变量关系、作用范围和函数中的变量与全局变量的关系、作用范围类似 '
>>> #1、嵌套函数可以直接使用主函数的变量
>>> #2、当嵌套函数使用主函数的变量时，如果不能使python解析器自动认定变量为主函数变量，可以使用nonlocal关键字标识主函数变量
>>> 

>>> #计算重力例子
>>> def weight(g):
	def cal_mg(m):
		return m*g
	return cal_mg

>>> w = weight(10) #g=10
>>> type(w)
<class 'function'>
>>> dir(w)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> mg = w(10)
>>> type(mg)
<class 'int'>
>>> mg
100
>>> print(mg)
100
"""
据说：执行w=weight(10)后，w所引用的是一个函数对象（cal_mg），而W(10)_则是向所引用的函数对象cal_mg传递了一个参数10，从而计算m*g并返回结果。
"""
>>> g0 = 9.78046 #赤道海平面上的重力加速度
>>> w0 = weight(g0)
>>> mg0 = w0(10)
>>> print(mg0）
	  
SyntaxError: invalid character in identifier
>>> print(mg0)
	  
97.8046
>>> ### 我目前没看懂这个例子？？？？？？？？？？？？？？？
	  
>>> ### 据说：这个嵌套函数，其实能够制作一个动态的函数对象——cal_mg。这个话题延伸下去，就是所谓的“闭包”。
	  
>>> ### 2018-1-9 22:27
	  
>>> 
	  
>>> 

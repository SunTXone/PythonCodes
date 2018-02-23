Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def package_position(*all_arguments):
	print(type(all_arguments))
	print(all_arguments)

	
>>> package_position(1,4,6)
<class 'tuple'>
(1, 4, 6)
>>> package_position(5,6,7,1,2,3)
<class 'tuple'>
(5, 6, 7, 1, 2, 3)
>>> package_position(1)
<class 'tuple'>
(1,)
>>> def package_keyword(**all_arguments):
	print(type(all_arguments))
	print(all_arguments)

	
>>> package_keyword(a=1,b=9)
<class 'dict'>
{'a': 1, 'b': 9}
>>> package_keyword(m=2,n=1,c='11')
<class 'dict'>
{'m': 2, 'n': 1, 'c': '11'}
>>> package_keyword(1,2,3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    package_keyword(1,2,3)
TypeError: package_keyword() takes 0 positional arguments but 3 were given
>>> def  package_mix(*positions,**keywords):
	print(type(positions))
	print(positions)
	print(type(keywords))
	print(keywords)

	
>>> package_mix(1,2,3,a=7,b=9,c=22)
<class 'tuple'>
(1, 2, 3)
<class 'dict'>
{'a': 7, 'b': 9, 'c': 22}
>>> package_mix(a=8,b=0)
<class 'tuple'>
()
<class 'dict'>
{'a': 8, 'b': 0}
>>> package_mix(1,2,3)
<class 'tuple'>
(1, 2, 3)
<class 'dict'>
{}
>>> #解包裹
>>> def unpackage(a,b,c):
	print(a,b,c)

	
>>> args = (1,2,3)
>>> unpackage(*args)
1 2 3
>>> #词典也可以用于解包裹
>>> args = {'a':1,'b':2,'c':3}
>>> unpackage(**args)
1 2 3
>>> 

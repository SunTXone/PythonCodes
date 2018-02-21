Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Foo:
	def bar(self):
		print("This is a normal method of class.")

		
>>>  f = Foo()
SyntaxError: unexpected indent
>>> f = Foo()
>>> f.bar()
This is a normal method of class.
>>> f.bar
<bound method Foo.bar of <__main__.Foo object at 0x0131FC10>>
>>> Foo.bar(m)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Foo.bar(m)
NameError: name 'm' is not defined
>>> Foo.bar(f)
This is a normal method of class.
>>> 
>>> 
>>> 
>>> Foo.bar
<function Foo.bar at 0x01852540>
>>> f.bar
<bound method Foo.bar of <__main__.Foo object at 0x0131FC10>>
>>> Foo.__dict__['bar']
<function Foo.bar at 0x01852540>
>>> Foo.__dict__['bar'].__get__(None,Foo)
<function Foo.bar at 0x01852540>
>>> Foo.__dict__['bar'].__get__(f,Foo)
<bound method Foo.bar of <__main__.Foo object at 0x0131FC10>>
>>> 

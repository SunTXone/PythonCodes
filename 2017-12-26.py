Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=input()
54
>>> a
'54'
>>> type(a)
<class 'str'>
>>> 
=================== RESTART: D:/PythonSpace/NameAgeTenn.py ===================
输入你的名字：孙同行
输入你的年龄：44
你的名字是“孙同行”。
你的年龄是44岁。
十年后你的年龄是54岁。
按回车结。
>>> dos="c:\news"
>>> dos
'c:\news'
>>> print(c)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(c)
NameError: name 'c' is not defined
>>> print(dos)
c:
ews
>>> dos="c:\\news"
>>> dos
'c:\\news'
>>> print(dos)
c:\news
>>> dos=r"c:\news"
>>> dos
'c:\\news'
>>> print(dos)
c:\news
>>> dos = r"c   \n news"
>>> dos
'c   \\n news'
>>> print(dos)
c   \n news
>>> dos="c  \n  news"
>>> dos
'c  \n  news'
>>> print(dos)
c  
  news
>>> str1='python'
>>> 'py' in str1
True
>>> 'th' in str1
True
>>> max(str1)
'y'
>>> min(str1)
'h'
>>> ord('h')
104
>>> chr(104)
'h'
>>> chr(105）
	
SyntaxError: invalid character in identifier
>>> chr(105)
	
'i'
>>> chr(103)
	
'g'
>>> ord('A')
	
65
>>> ord('a')
	
97
>>> chr(90)
	
'Z'
>>> print("Ab"*3)
	
AbAbAb
>>> len(str1)
	
6
>>> help(len)
	
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> help(len)
	
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> help(print)
	
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> "I like {0} and {1}.".format("大泽","孙晟睿")
	
'I like 大泽 and 孙晟睿.'
>>> myLike=["田莹","大泽","孙晟睿"]
	
>>> myLike
	
['田莹', '大泽', '孙晟睿']
>>> "I like {0},{1} and {2}.}.format(myLike)
	
SyntaxError: EOL while scanning string literal
>>> "She is {0:d} years old and the breast is {1:f}cm.".format(18,92.88)
	
'She is 18 years old and the breast is 92.880000cm.'
>>> "She is {0:d} years old and the breast is {1:f.2}cm.".format(18,92.88)
	
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    "She is {0:d} years old and the breast is {1:f.2}cm.".format(18,92.88)
ValueError: Invalid format specifier
>>> "She is {0:4d} years old and the breast is {1:6.2f}cm.".format(18,92.88)
	
'She is   18 years old and the breast is  92.88cm.'
>>> "She is {0:<4d} years old and the breast is {1:^9.2f}cm.".format(18,92.88)
	
'She is 18   years old and the breast is   92.88  cm.'
>>> "She is {0:<04d} years old and the breast is {1:^09.2f}cm.".format(18,92.88)
	
'She is 1800 years old and the breast is 0092.8800cm.'
>>> "She is {0:4d} years old and the breast is {1:^9.2f}cm.".format(18,92.88)
	
'She is   18 years old and the breast is   92.88  cm.'
>>> "She is {0:04d} years old and the breast is {1:^09.2f}cm.".format(18,92.88)
	
'She is 0018 years old and the breast is 0092.8800cm.'
>>> 

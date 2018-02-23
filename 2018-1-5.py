Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3)
>>> b=(4,5,6)
>>> c=[]
>>> for x,y in zip(a,b):
	c.append(x+y)

	
>>> c
[5, 7, 9]
>>> x
3
>>> y
6
>>> z1=0
>>> z2=9
>>> d=[]
>>> for z1,z2 in zip(a,b):
	d.append(z1+z2)

	
>>> z1
3
>>> z2
6
>>> d
[5, 7, 9]
>>> i=9
>>> for i in range(8)
SyntaxError: invalid syntax
>>> for i in range(8):
	print(i)

	
0
1
2
3
4
5
6
7
>>> i
7
>>> for x in a:
	print(x)

	
1
2
3
>>> w='string'
>>> for x in w:
	print(x)

	
s
t
r
i
n
g

>>> grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
>>> grid
[['.', '.', '.', '.', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['O', 'O', 'O', 'O', 'O', '.'], ['.', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]
>>> len(grid)
9
>>> ''.join(grid[1])
'.OO...'
>>> for i in grid:
	print(''.join(i))

	
......
.OO...
OOOO..
OOOOO.
.OOOOO
OOOOO.
OOOO..
.OO...
......
>>> len(grid[0])
6
>>> for i in range(len(grid[0])):
	for j in range(len(grid)):
		print(grid[j][i],sep='',end='')
	print('\n',sep='',end='')

	
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
>>> #逗号代码
>>> spam=['apples
	  
SyntaxError: EOL while scanning string literal
>>> spam=['apples','bananas','tofu','cats']
	  
>>> #编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。例如，将前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。
	  
>>> def joinStr(list):
	  str=''
	  for x in list:



	      ;
	  
SyntaxError: invalid syntax
>>> 
	  
>>> def joinStr(list):
    str=''
	for i in range(len(list)):
	    if i == 0 :
		    str+=list[i]
		elif i==len(list)-1:
		    str+=('and '+list(i))
		else:
		    str+=(','+list(i))
	return str 

	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def joinStr(list):
    str=''
    for i in range(len(list)):
        if i == 0 :
            str+=list[i]
        elif i==len(list)-1:
            str+=('and '+list(i))
        else:
            str+=(','+list(i))
    return str

>>> mystr=joinStr(spam)
	  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    mystr=joinStr(spam)
  File "<pyshell#57>", line 9, in joinStr
    str+=(','+list(i))
TypeError: 'list' object is not callable
>>> mystr=[]
	  
>>> mystr=joinStr(spam)
	  
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    mystr=joinStr(spam)
  File "<pyshell#57>", line 9, in joinStr
    str+=(','+list(i))
TypeError: 'list' object is not callable
>>> joinStr(spam)
	  
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    joinStr(spam)
  File "<pyshell#57>", line 9, in joinStr
    str+=(','+list(i))
TypeError: 'list' object is not callable
>>> def joinStr(list):
    str=''
    for i in range(len(list)):
        if i == 0 :
            str+=list[i]
        elif i==len(list)-1:
            str+=('and '+list(i))
        else:
            str+=(','+list(i))
    print str
	  
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(int str)?
>>> print spam
	  
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(spam)?
>>> print(spam)
	  
['apples', 'bananas', 'tofu', 'cats']
>>> def joinStr(list):
    str=''
    for i in range(len(list)):
        if i == 0 :
            str+=list[i]
        elif i==len(list)-1:
            str+=('and '+list(i))
        else:
            str+=(','+list(i))
    print(str)

	  
>>> joinStr(spam)
	  
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    joinStr(spam)
  File "<pyshell#66>", line 9, in joinStr
    str+=(','+list(i))
TypeError: 'list' object is not callable
>>> 

>>> dir()
	  
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'd', 'grid', 'i', 'j', 'joinStr', 'mystr', 'spam', 'w', 'x', 'y', 'z1', 'z2']
>>> z1
	  
3
>>> spam
	  
['apples', 'bananas', 'tofu', 'cats']
>>> joinStr(spam)
	  
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    joinStr(spam)
  File "<pyshell#66>", line 9, in joinStr
    str+=(','+list(i))
TypeError: 'list' object is not callable
>>> def eggs(someParameter):
	  someParameter.append('Hello')

	  
>>> spam
	  
['apples', 'bananas', 'tofu', 'cats']
>>> eggs(spam)
	  
>>> print(spam)
	  
['apples', 'bananas', 'tofu', 'cats', 'Hello']
>>> def p1(l):
    str=''.join(l)
    print(str)

>>> 
p1(spam)
	  
applesbananastofucatsHello
>>> del p1
	  
>>> def p1(l):
    str=','.join(l)
    print(str)

>>> p1(spam)
	  
apples,bananas,tofu,cats,Hello
>>> def p2(l)
    str =''
    for i = range(len(l)):
	    str = str +','+l(i)
	print(str)
	  
SyntaxError: invalid syntax
>>> def p2(l):
    str =''
    for i = range(len(l)):
	    str = str +','+l(i)
	print(str)
	  
SyntaxError: invalid syntax
>>> 
	  
>>> def p2(l):
    str =''
    for i in range(len(l)):
	    str = str +','+l(i)
	print(str)
	  
SyntaxError: unindent does not match any outer indentation level
>>> def p2(l):
    str =''
    for i in range(len(l)):
	    str = str +','+l(i)
    print(str)

	  
>>> p2(spam)
	  
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    p2(spam)
  File "<pyshell#89>", line 4, in p2
    str = str +','+l(i)
TypeError: 'list' object is not callable
>>> 

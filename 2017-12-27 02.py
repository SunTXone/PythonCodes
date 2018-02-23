Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> la=[1,2,3]
>>> lb='abc'
>>> la.extend(lb)
>>> la
[1, 2, 3, 'a', 'b', 'c']
>>> id(lb)
42565056
>>> lb=['qiwsir','python']
>>> id(lb)
55529680
>>> id(la)
55307240
>>> la[len(la):]=lb
>>> la
[1, 2, 3, 'a', 'b', 'c', 'qiwsir', 'python']
>>> id(la）
       
SyntaxError: invalid character in identifier
>>> id(la)
       
55307240
>>> dir(str)
       
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(int)
       
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(float)
       
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> lc='aabbbccccddddd'
       
>>> lc.count('a')
       
2
>>> lc.count('b')
       
3
>>> lc.count('d')
       
5
>>> lc.count(1)
       
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    lc.count(1)
TypeError: must be str, not int
>>> lc.count('f')
       
0
>>> help(str.index)
       
Help on method_descriptor:

index(...)
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found, 
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.

>>> lc.index('a')
       
0
>>> lc.index('d')
       
9
>>> lc.index('d
	     
SyntaxError: EOL while scanning string literal
>>> lc.index('d',10)
	     
10
>>> lc.index('d',10,15)
	     
10
>>> help(list.index)
	     
Help on method_descriptor:

index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> help(list.insert)
	     
Help on method_descriptor:

insert(...)
    L.insert(index, object) -- insert object before index

>>> a=[1,2,3]
	     
>>> a.insert(len(a),4)
	     
>>> a
	     
[1, 2, 3, 4]
>>> a.insert(9,5)
	     
>>> a
	     
[1, 2, 3, 4, 5]
>>> help(list.insert)
	     
Help on method_descriptor:

insert(...)
    L.insert(index, object) -- insert object before index

>>> help(list.remove)
	     
Help on method_descriptor:

remove(...)
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.

>>> help(list.pop)
	     
Help on method_descriptor:

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

>>> a
	     
[1, 2, 3, 4, 5]
>>> a.pop(0)
	     
1
>>> a
	     
[2, 3, 4, 5]
>>> a.pop(2)
	     
4
>>> a
	     
[2, 3, 5]
>>> a.pop()
	     
5
>>> a
	     
[2, 3]
>>> dir(list)
	     
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(in)
	     
SyntaxError: invalid syntax
>>> a
	     
[2, 3]
>>> if 2 in a :
	     a.remove(2)
	     print(a)
	     else:
	     
SyntaxError: invalid syntax
>>> a
	     
[2, 3]
>>> a.insert(9,0)
	     
>>> a.insert(10,7)
	     
>>> if 2 in a:
	a.remove(2)
	print(a)
else:
	     print( ' 2 not in a ')

	     
[3, 0, 7]
>>> print(a.pop(1))
	     
0
>>> a
	     
[3, 7]
>>> help(list.reverse)
	     
Help on method_descriptor:

reverse(...)
    L.reverse() -- reverse *IN PLACE*

>>> help(str.reverse)
	     
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    help(str.reverse)
AttributeError: type object 'str' has no attribute 'reverse'
>>> a
	     
[3, 7]
>>> a.reverse
	     
<built-in method reverse of list object at 0x034E8170>
>>> a
	     
[3, 7]
>>> a.reverse()
	     
>>> a
	     
[7, 3]
>>> a.reversed()
	     
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.reversed()
AttributeError: 'list' object has no attribute 'reversed'
>>> help(reversed)
	     
Help on class reversed in module builtins:

class reversed(object)
 |  reversed(sequence) -> reverse iterator over values of the sequence
 |  
 |  Return a reverse iterator
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __length_hint__(...)
 |      Private method returning an estimate of len(list(it)).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __setstate__(...)
 |      Set state information for unpickling.

>>> help(id)
	     
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> id(a)
     
55476592
>>> a
     
[7, 3]
>>> a.reserve()
     
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.reserve()
AttributeError: 'list' object has no attribute 'reserve'
>>> a.reserve()
     
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.reserve()
AttributeError: 'list' object has no attribute 'reserve'
>>> a.reverse()
     
>>> a
     
[3, 7]
>>> id(a)
     
55476592
>>> help(str.sort)
     
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    help(str.sort)
AttributeError: type object 'str' has no attribute 'sort'
>>> help(list.sort)
     
Help on method_descriptor:

sort(...)
    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

>>> a
     
[3, 7]
>>> a.reverse()
     
>>> a
     
[7, 3]
>>> a.sort()
     
>>> a
     
[3, 7]
>>> a.sort(reverse=True)
     
>>> a
     
[7, 3]
>>> a.sort(key=None,True)
     
SyntaxError: positional argument follows keyword argument
>>> a.sort(key=None)
     
>>> a
     
[3, 7]
>>> a.sort(None,True)
     
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.sort(None,True)
TypeError: must use keyword argument for key function
>>> a.sort(key=None,reverse=True)
     
>>> a
     
[7, 3]
>>> a.sort(key=none)
     
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.sort(key=none)
NameError: name 'none' is not defined
>>> a.sort(reverse=false)
     
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.sort(reverse=false)
NameError: name 'false' is not defined
>>> help(sorted)
     
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

>>> import keyword
     
>>> keyword.kwlist
     
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> help(id)
     
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> help(type)
     
Help on class type in module builtins:

class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
 |  
 |  Methods defined here:
 |  
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __dir__(...)
 |      __dir__() -> list
 |      specialized __dir__ implementation for types
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __instancecheck__(...)
 |      __instancecheck__() -> bool
 |      check if an object is an instance
 |  
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __prepare__(...)
 |      __prepare__() -> dict
 |      used to create the namespace for the class statement
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __sizeof__(...)
 |      __sizeof__() -> int
 |      return memory consumption of the type object
 |  
 |  __subclasscheck__(...)
 |      __subclasscheck__() -> bool
 |      check if a class is a subclass
 |  
 |  __subclasses__(...)
 |      __subclasses__() -> list of immediate subclasses
 |  
 |  mro(...)
 |      mro() -> list
 |      return a type's method resolution order
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __abstractmethods__
 |  
 |  __dict__
 |  
 |  __text_signature__
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __base__ = <class 'object'>
 |      The most base type
 |  
 |  __bases__ = (<class 'object'>,)
 |  
 |  __basicsize__ = 432
 |  
 |  __dictoffset__ = 132
 |  
 |  __flags__ = -2146675712
 |  
 |  __itemsize__ = 20
 |  
 |  __mro__ = (<class 'type'>, <class 'object'>)
 |  
 |  __weakrefoffset__ = 184

>>> help(dir)
     
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

>>> dir()
     
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'keyword', 'la', 'lb', 'lc']
>>> keyword
     
<module 'keyword' from 'C:\\Python364-32\\lib\\keyword.py'>
>>> dir(keyword)
     
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'iskeyword', 'kwlist', 'main']
>>> dir()
     
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'keyword', 'la', 'lb', 'lc']
>>> a
     
[7, 3]
>>> la
     
[1, 2, 3, 'a', 'b', 'c', 'qiwsir', 'python']
>>> lc
     
'aabbbccccddddd'
>>> lb
     
['qiwsir', 'python']
>>> sb='You are a hero ?'
     
>>> help(str.split)
     
Help on method_descriptor:

split(...)
    S.split(sep=None, maxsplit=-1) -> list of strings
    
    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.

>>> help(list.join)
     
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    help(list.join)
AttributeError: type object 'list' has no attribute 'join'
>>> help(join)
     
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    help(join)
NameError: name 'join' is not defined
>>> help(str.join)
     
Help on method_descriptor:

join(...)
    S.join(iterable) -> str
    
    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.

>>> sb
     
'You are a hero ?'
>>> sc = 'You \nare\ta hero ?'
     
>>> id(sb)
     
8327200
>>> id(sc)
     
8327632
>>> sb.split()
     
['You', 'are', 'a', 'hero', '?']
>>> id(sb)
     
8327200
>>> sc.split()
     
['You', 'are', 'a', 'hero', '?']
>>> id(sc)
     
8327632
>>> sc.split(' ')
     
['You', '\nare\ta', 'hero', '?']
>>> sc2=sc.split(' ')
     
>>> sc2
     
['You', '\nare\ta', 'hero', '?']
>>> sc2[1]
     
'\nare\ta'
>>> print(sc2[1])
     

are	a
>>> id(sc2)
     
55477312
>>> ' '.join(sc2)
     
'You \nare\ta hero ?'
>>> print('
	  
SyntaxError: EOL while scanning string literal
>>> print(' '.join(sc2)
	  )
	  
You 
are	a hero ?
>>> sc3=' '.join(sc2)
	  
>>> sc3
	  
'You \nare\ta hero ?'
>>> print(sc3)
	  
You 
are	a hero ?
>>> dir()
	  
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'keyword', 'la', 'lb', 'lc', 'sb', 'sc', 'sc2', 'sc3']
>>> t=123,'abc',['come','here']
	  
>>> t
	  
(123, 'abc', ['come', 'here'])
>>> dir(tuple)
	  
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> help(tuple.count)
	  
Help on method_descriptor:

count(...)
    T.count(value) -> integer -- return number of occurrences of value

>>> help(tuple.index)
	  
Help on method_descriptor:

index(...)
    T.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> 

Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: D:/PythonSpace/magic8Ball.py ===================
Yes
>>> 
=================== RESTART: D:/PythonSpace/magic8Ball.py ===================
Ask again later
>>> 
=================== RESTART: D:/PythonSpace/magic8Ball.py ===================
It is decidedly so
>>> 
=================== RESTART: D:/PythonSpace/magic8Ball.py ===================
Very doubtful
>>> 
=================== RESTART: D:/PythonSpace/magic8Ball.py ===================
Concentrate and ask again
>>> 
=================== RESTART: D:/PythonSpace/magic8Ball.py ===================
Yes
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fortune', 'getAnswer', 'r', 'random']
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

>>> print('I','am','a','goodman')
I am a goodman
>>>  print('I','am','a','goodman',end='!\n')
SyntaxError: unexpected indent
>>> print('I','am','a','goodman',end='!\n')
I am a goodman!
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fortune', 'getAnswer', 'r', 'random']
>>> del r
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fortune', 'getAnswer', 'random']
>>> del random
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fortune', 'getAnswer']
>>> del getAnswer
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fortune']
>>> del fortune
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
>>> def spam(divideBy)
SyntaxError: invalid syntax
>>> def spam(divideBy):
	return 42/divideBy

>>> print(spam(2))
21.0
>>> print(spam(12))
3.5
>>> print(spam(0))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(spam(0))
  File "<pyshell#17>", line 2, in spam
    return 42/divideBy
ZeroDivisionError: division by zero
>>> print(spam(1))
42.0
>>> print(spam('a'))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(spam('a'))
  File "<pyshell#17>", line 2, in spam
    return 42/divideBy
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> del spam
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

>>> def spam(divideBy):
	try:
		return(42/divideBy)
	except ZeroDivisionError:
		print('Error:Invalid argument.')

		
>>> print(spam(2))
21.0
>>> print(spam(12))
3.5
>>> print(spam(0))
Error:Invalid argument.
None
>>> print(spam(1))
42.0
>>> print(spam('a'))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(spam('a'))
  File "<pyshell#30>", line 3, in spam
    return(42/divideBy)
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> 

>>> 
================= RESTART: D:/PythonSpace/guessTheNumber.py =================
I am thinking of a number between 1 and 20.
Take a guess.
5
Youre guess is too high.
Take a guess.
3
Good job! You  guessed my number in 2 guesses!
>>> 
================= RESTART: D:/PythonSpace/guessTheNumber.py =================
I am thinking of a number between 1 and 20.
Take a guess.
q10
Traceback (most recent call last):
  File "D:/PythonSpace/guessTheNumber.py", line 9, in <module>
    guess = int(input())
ValueError: invalid literal for int() with base 10: 'q10'
>>> 
================= RESTART: D:/PythonSpace/guessTheNumber.py =================
I am thinking of a number between 1 and 20.
Take a guess.
10
Youre guess is too high.
Take a guess.
5
Youre guess is too high.
Take a guess.
3
Youre guess is too high.
Take a guess.
2
Good job! You  guessed my number in 4 guesses!
>>> help(int)
Help on class int in module builtins:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |      default object formatter
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      Returns size in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  from_bytes(...) from builtins.type
 |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
 |      
 |      Return the integer represented by the given array of bytes.
 |      
 |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument indicates whether two's complement is
 |      used to represent the integer.
 |  
 |  to_bytes(...)
 |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
 |      
 |      Return an array of bytes representing an integer.
 |      
 |      The integer is represented using length bytes.  An OverflowError is
 |      raised if the integer is not representable with the given number of
 |      bytes.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument determines whether two's complement is
 |      used to represent the integer.  If signed is False and a negative integer
 |      is given, an OverflowError is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> 
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:4
4
2
2
1
1
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:77
77
232
232
116
116
58
58
29
29
88
88
44
44
22
22
11
11
34
34
17
17
52
52
26
26
13
13
40
40
20
20
10
10
5
5
16
16
8
8
4
4
2
2
1
1
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:75
75
226
113
340
170
85
256
128
64
32
16
8
4
2
1
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:690
690
345
1036
518
259
778
389
1168
584
292
146
73
220
110
55
166
83
250
125
376
188
94
47
142
71
214
107
322
161
484
242
121
364
182
91
274
137
412
206
103
310
155
466
233
700
350
175
526
263
790
395
1186
593
1780
890
445
1336
668
334
167
502
251
754
377
1132
566
283
850
425
1276
638
319
958
479
1438
719
2158
1079
3238
1619
4858
2429
7288
3644
1822
911
2734
1367
4102
2051
6154
3077
9232
4616
2308
1154
577
1732
866
433
1300
650
325
976
488
244
122
61
184
92
46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:qq
Traceback (most recent call last):
  File "D:/PythonSpace/collatz.py", line 12, in <module>
    num=int(input('Enter number:'))
ValueError: invalid literal for int() with base 10: 'qq'
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:q
You must input a integer!
Traceback (most recent call last):
  File "D:/PythonSpace/collatz.py", line 16, in <module>
    print(num)
NameError: name 'num' is not defined
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:e
You must input a integer!
>>> 
===================== RESTART: D:/PythonSpace/collatz.py =====================
Enter number:111
111
334
167
502
251
754
377
1132
566
283
850
425
1276
638
319
958
479
1438
719
2158
1079
3238
1619
4858
2429
7288
3644
1822
911
2734
1367
4102
2051
6154
3077
9232
4616
2308
1154
577
1732
866
433
1300
650
325
976
488
244
122
61
184
92
46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
>>> 

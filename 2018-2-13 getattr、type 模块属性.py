Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os,sys
>>> name_list = dir(__builtin__)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name_list = dir(__builtin__)
NameError: name '__builtin__' is not defined
>>> name_list = dir('__builtin__')
>>> name_list
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> for i in name_list:
	print(__builtin__[i])

	
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    print(__builtin__[i])
NameError: name '__builtin__' is not defined
>>> __builtin__.__dir__[tupel]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    __builtin__.__dir__[tupel]
NameError: name '__builtin__' is not defined
>>> __builtin__
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    __builtin__
NameError: name '__builtin__' is not defined
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'i', 'name_list', 'os', 'sys']
>>> __builtins__[tuple]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    __builtins__[tuple]
TypeError: 'module' object is not subscriptable
>>> __builtins__['tuple']
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    __builtins__['tuple']
TypeError: 'module' object is not subscriptable
>>> __builtins__.__dir__['tuple']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    __builtins__.__dir__['tuple']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> __builtins__.__dir__
<built-in function __dir__>
>>> 
=============================== RESTART: Shell ===============================
>>> import sys
>>> modulelist= dirO(module_)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    modulelist= dirO(module_)
NameError: name 'dirO' is not defined
>>> modulelist = dir(module_)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    modulelist = dir(module_)
NameError: name 'module_' is not defined
>>> modulelist = dir(module)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    modulelist = dir(module)
NameError: name 'module' is not defined
>>> modulelist = dir(_module_)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    modulelist = dir(_module_)
NameError: name '_module_' is not defined
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sys']
>>> name_list = dir('__builtins__')
>>> length = len(name_list)
>>> for i in range(0,length):
	print getattr('__builtins__',name_list[i]
		      
SyntaxError: invalid syntax
>>> import sys
		      
>>> for i in range(0,length):
	print getattr('__builtins__',name_list[i]
		      
SyntaxError: invalid syntax
>>> help(sys.getattr)
		      
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    help(sys.getattr)
AttributeError: module 'sys' has no attribute 'getattr'
>>> help(getattr)
		      
Help on built-in function getattr in module builtins:

getattr(...)
    getattr(object, name[, default]) -> value
    
    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.

>>> name_list
		      
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> name_list[5]
		      
'__doc__'
>>> name_list[15]
		      
'__init_subclass__'
>>> getattr(__builtins__,name_list[15])
		      
<built-in method __init_subclass__ of type object at 0x00000000616DA020>
>>> getattr('__builtins__',name_list[15])
		      
<built-in method __init_subclass__ of type object at 0x00000000616DCF30>
>>> help('__builtins__.__doc__')
		      
No Python documentation found for '__builtins__.__doc__'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> def print_all(module_):
		      modulelist = dir(module_)
		      length = len(modulelist)
		      for i in range(0,length):
		          print(getattr(module_,modulelist[i]))

		      
>>> import sys
		      
>>> print_all(sys)
		      
<built-in function displayhook>
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a struct sequence with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a struct sequence with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a struct sequence with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a struct sequence with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
_enablelegacywindowsfsencoding -- [Windows only] 
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setcheckinterval() -- control how often the interpreter checks for events
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function

<built-in function excepthook>
<function enablerlcompleter.<locals>.register_readline at 0x00000154726A17B8>
<class '_frozen_importlib.BuiltinImporter'>
sys

ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>)
None
None
None
<built-in function _clear_type_cache>
<built-in function _current_frames>
<built-in function _debugmallocstats>
<built-in function _enablelegacywindowsfsencoding>
<built-in function _getframe>
('CPython', 'v3.6.4', 'd48eceb')
None
{}
1013
['']
D:\Python36x64
D:\Python36x64
('_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_csv', '_datetime', '_findvs', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zipimport', 'zlib')
little
<built-in function call_tracing>
<built-in function callstats>
Copyright (c) 2001-2017 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
<function displayhook at 0x0000015472D4EB70>
1631518720
False
<built-in function exc_info>
<built-in function excepthook>
D:\Python36x64
D:\Python36x64\pythonw.exe
<built-in function exit>
sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0)
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
short
<built-in function get_asyncgen_hooks>
<built-in function get_coroutine_wrapper>
<built-in function getallocatedblocks>
<built-in function getcheckinterval>
<built-in function getdefaultencoding>
<built-in function getfilesystemencodeerrors>
<built-in function getfilesystemencoding>
<built-in function getprofile>
<built-in function getrecursionlimit>
<built-in function getrefcount>
<built-in function getsizeof>
<built-in function getswitchinterval>
<built-in function gettrace>
<built-in function getwindowsversion>
sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)
50726128
namespace(cache_tag='cpython-36', hexversion=50726128, name='cpython', version=sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0))
sys.int_info(bits_per_digit=30, sizeof_digit=4)
<built-in function intern>
<built-in function is_finalizing>
<traceback object at 0x0000015472ED5488>
<class 'AttributeError'>
module 'sys' has no attribute 'getattr'
9223372036854775807
1114111
[<class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>]
{'builtins': <module 'builtins' (built-in)>, 'sys': <module 'sys' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_thread': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'nt': <module 'nt' (built-in)>, 'winreg': <module 'winreg' (built-in)>, 'zipimport': <module 'zipimport' (built-in)>, 'encodings': <module 'encodings' from 'D:\\Python36x64\\lib\\encodings\\__init__.py'>, 'codecs': <module 'codecs' from 'D:\\Python36x64\\lib\\codecs.py'>, '_codecs': <module '_codecs' (built-in)>, 'encodings.aliases': <module 'encodings.aliases' from 'D:\\Python36x64\\lib\\encodings\\aliases.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from 'D:\\Python36x64\\lib\\encodings\\utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' (built-in)>, 'encodings.latin_1': <module 'encodings.latin_1' from 'D:\\Python36x64\\lib\\encodings\\latin_1.py'>, 'io': <module 'io' from 'D:\\Python36x64\\lib\\io.py'>, 'abc': <module 'abc' from 'D:\\Python36x64\\lib\\abc.py'>, '_weakrefset': <module '_weakrefset' from 'D:\\Python36x64\\lib\\_weakrefset.py'>, 'site': <module 'site' from 'D:\\Python36x64\\lib\\site.py'>, 'os': <module 'os' from 'D:\\Python36x64\\lib\\os.py'>, 'errno': <module 'errno' (built-in)>, 'stat': <module 'stat' from 'D:\\Python36x64\\lib\\stat.py'>, '_stat': <module '_stat' (built-in)>, 'ntpath': <module 'ntpath' from 'D:\\Python36x64\\lib\\ntpath.py'>, 'genericpath': <module 'genericpath' from 'D:\\Python36x64\\lib\\genericpath.py'>, 'os.path': <module 'ntpath' from 'D:\\Python36x64\\lib\\ntpath.py'>, '_collections_abc': <module '_collections_abc' from 'D:\\Python36x64\\lib\\_collections_abc.py'>, '_sitebuiltins': <module '_sitebuiltins' from 'D:\\Python36x64\\lib\\_sitebuiltins.py'>, 'sysconfig': <module 'sysconfig' from 'D:\\Python36x64\\lib\\sysconfig.py'>, 'idlelib': <module 'idlelib' from 'D:\\Python36x64\\lib\\idlelib\\__init__.py'>, 'idlelib.run': <module 'idlelib.run' from 'D:\\Python36x64\\lib\\idlelib\\run.py'>, 'linecache': <module 'linecache' from 'D:\\Python36x64\\lib\\linecache.py'>, 'functools': <module 'functools' from 'D:\\Python36x64\\lib\\functools.py'>, '_functools': <module '_functools' (built-in)>, 'collections': <module 'collections' from 'D:\\Python36x64\\lib\\collections\\__init__.py'>, 'operator': <module 'operator' from 'D:\\Python36x64\\lib\\operator.py'>, '_operator': <module '_operator' (built-in)>, 'keyword': <module 'keyword' from 'D:\\Python36x64\\lib\\keyword.py'>, 'heapq': <module 'heapq' from 'D:\\Python36x64\\lib\\heapq.py'>, '_heapq': <module '_heapq' (built-in)>, 'itertools': <module 'itertools' (built-in)>, 'reprlib': <module 'reprlib' from 'D:\\Python36x64\\lib\\reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'types': <module 'types' from 'D:\\Python36x64\\lib\\types.py'>, 'collections.abc': <module 'collections.abc' from 'D:\\Python36x64\\lib\\collections\\abc.py'>, 'weakref': <module 'weakref' from 'D:\\Python36x64\\lib\\weakref.py'>, 'tokenize': <module 'tokenize' from 'D:\\Python36x64\\lib\\tokenize.py'>, 're': <module 're' from 'D:\\Python36x64\\lib\\re.py'>, 'enum': <module 'enum' from 'D:\\Python36x64\\lib\\enum.py'>, 'sre_compile': <module 'sre_compile' from 'D:\\Python36x64\\lib\\sre_compile.py'>, '_sre': <module '_sre' (built-in)>, 'sre_parse': <module 'sre_parse' from 'D:\\Python36x64\\lib\\sre_parse.py'>, 'sre_constants': <module 'sre_constants' from 'D:\\Python36x64\\lib\\sre_constants.py'>, '_locale': <module '_locale' (built-in)>, 'copyreg': <module 'copyreg' from 'D:\\Python36x64\\lib\\copyreg.py'>, 'token': <module 'token' from 'D:\\Python36x64\\lib\\token.py'>, 'queue': <module 'queue' from 'D:\\Python36x64\\lib\\queue.py'>, 'threading': <module 'threading' from 'D:\\Python36x64\\lib\\threading.py'>, 'time': <module 'time' (built-in)>, 'traceback': <module 'traceback' from 'D:\\Python36x64\\lib\\traceback.py'>, 'warnings': <module 'warnings' from 'D:\\Python36x64\\lib\\warnings.py'>, 'tkinter': <module 'tkinter' from 'D:\\Python36x64\\lib\\tkinter\\__init__.py'>, '_tkinter': <module '_tkinter' from 'D:\\Python36x64\\DLLs\\_tkinter.pyd'>, 'tkinter.constants': <module 'tkinter.constants' from 'D:\\Python36x64\\lib\\tkinter\\constants.py'>, 'idlelib.autocomplete': <module 'idlelib.autocomplete' from 'D:\\Python36x64\\lib\\idlelib\\autocomplete.py'>, 'string': <module 'string' from 'D:\\Python36x64\\lib\\string.py'>, '_string': <module '_string' (built-in)>, 'idlelib.autocomplete_w': <module 'idlelib.autocomplete_w' from 'D:\\Python36x64\\lib\\idlelib\\autocomplete_w.py'>, 'platform': <module 'platform' from 'D:\\Python36x64\\lib\\platform.py'>, 'subprocess': <module 'subprocess' from 'D:\\Python36x64\\lib\\subprocess.py'>, 'signal': <module 'signal' from 'D:\\Python36x64\\lib\\signal.py'>, 'msvcrt': <module 'msvcrt' (built-in)>, '_winapi': <module '_winapi' (built-in)>, 'idlelib.multicall': <module 'idlelib.multicall' from 'D:\\Python36x64\\lib\\idlelib\\multicall.py'>, 'idlelib.config': <module 'idlelib.config' from 'D:\\Python36x64\\lib\\idlelib\\config.py'>, 'configparser': <module 'configparser' from 'D:\\Python36x64\\lib\\configparser.py'>, '_bootlocale': <module '_bootlocale' from 'D:\\Python36x64\\lib\\_bootlocale.py'>, 'encodings.gbk': <module 'encodings.gbk' from 'D:\\Python36x64\\lib\\encodings\\gbk.py'>, '_codecs_cn': <module '_codecs_cn' (built-in)>, '_multibytecodec': <module '_multibytecodec' (built-in)>, 'idlelib.hyperparser': <module 'idlelib.hyperparser' from 'D:\\Python36x64\\lib\\idlelib\\hyperparser.py'>, 'idlelib.pyparse': <module 'idlelib.pyparse' from 'D:\\Python36x64\\lib\\idlelib\\pyparse.py'>, 'idlelib.calltips': <module 'idlelib.calltips' from 'D:\\Python36x64\\lib\\idlelib\\calltips.py'>, 'inspect': <module 'inspect' from 'D:\\Python36x64\\lib\\inspect.py'>, 'ast': <module 'ast' from 'D:\\Python36x64\\lib\\ast.py'>, '_ast': <module '_ast' (built-in)>, 'dis': <module 'dis' from 'D:\\Python36x64\\lib\\dis.py'>, 'opcode': <module 'opcode' from 'D:\\Python36x64\\lib\\opcode.py'>, '_opcode': <module '_opcode' (built-in)>, 'importlib': <module 'importlib' from 'D:\\Python36x64\\lib\\importlib\\__init__.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'importlib.machinery': <module 'importlib.machinery' from 'D:\\Python36x64\\lib\\importlib\\machinery.py'>, 'textwrap': <module 'textwrap' from 'D:\\Python36x64\\lib\\textwrap.py'>, 'idlelib.calltip_w': <module 'idlelib.calltip_w' from 'D:\\Python36x64\\lib\\idlelib\\calltip_w.py'>, 'idlelib.debugger_r': <module 'idlelib.debugger_r' from 'D:\\Python36x64\\lib\\idlelib\\debugger_r.py'>, 'idlelib.debugger': <module 'idlelib.debugger' from 'D:\\Python36x64\\lib\\idlelib\\debugger.py'>, 'bdb': <module 'bdb' from 'D:\\Python36x64\\lib\\bdb.py'>, 'fnmatch': <module 'fnmatch' from 'D:\\Python36x64\\lib\\fnmatch.py'>, 'posixpath': <module 'posixpath' from 'D:\\Python36x64\\lib\\posixpath.py'>, 'idlelib.macosx': <module 'idlelib.macosx' from 'D:\\Python36x64\\lib\\idlelib\\macosx.py'>, 'idlelib.scrolledlist': <module 'idlelib.scrolledlist' from 'D:\\Python36x64\\lib\\idlelib\\scrolledlist.py'>, 'idlelib.windows': <module 'idlelib.windows' from 'D:\\Python36x64\\lib\\idlelib\\windows.py'>, 'idlelib.debugobj_r': <module 'idlelib.debugobj_r' from 'D:\\Python36x64\\lib\\idlelib\\debugobj_r.py'>, 'idlelib.rpc': <module 'idlelib.rpc' from 'D:\\Python36x64\\lib\\idlelib\\rpc.py'>, 'pickle': <module 'pickle' from 'D:\\Python36x64\\lib\\pickle.py'>, 'struct': <module 'struct' from 'D:\\Python36x64\\lib\\struct.py'>, '_struct': <module '_struct' (built-in)>, '_compat_pickle': <module '_compat_pickle' from 'D:\\Python36x64\\lib\\_compat_pickle.py'>, '_pickle': <module '_pickle' (built-in)>, 'select': <module 'select' from 'D:\\Python36x64\\DLLs\\select.pyd'>, 'socket': <module 'socket' from 'D:\\Python36x64\\lib\\socket.py'>, '_socket': <module '_socket' from 'D:\\Python36x64\\DLLs\\_socket.pyd'>, 'selectors': <module 'selectors' from 'D:\\Python36x64\\lib\\selectors.py'>, 'math': <module 'math' (built-in)>, 'socketserver': <module 'socketserver' from 'D:\\Python36x64\\lib\\socketserver.py'>, 'idlelib.iomenu': <module 'idlelib.iomenu' from 'D:\\Python36x64\\lib\\idlelib\\iomenu.py'>, 'shlex': <module 'shlex' from 'D:\\Python36x64\\lib\\shlex.py'>, 'tempfile': <module 'tempfile' from 'D:\\Python36x64\\lib\\tempfile.py'>, 'shutil': <module 'shutil' from 'D:\\Python36x64\\lib\\shutil.py'>, 'zlib': <module 'zlib' (built-in)>, 'bz2': <module 'bz2' from 'D:\\Python36x64\\lib\\bz2.py'>, '_compression': <module '_compression' from 'D:\\Python36x64\\lib\\_compression.py'>, '_bz2': <module '_bz2' from 'D:\\Python36x64\\DLLs\\_bz2.pyd'>, 'lzma': <module 'lzma' from 'D:\\Python36x64\\lib\\lzma.py'>, '_lzma': <module '_lzma' from 'D:\\Python36x64\\DLLs\\_lzma.pyd'>, 'random': <module 'random' from 'D:\\Python36x64\\lib\\random.py'>, 'hashlib': <module 'hashlib' from 'D:\\Python36x64\\lib\\hashlib.py'>, '_hashlib': <module '_hashlib' from 'D:\\Python36x64\\DLLs\\_hashlib.pyd'>, '_blake2': <module '_blake2' (built-in)>, '_sha3': <module '_sha3' (built-in)>, 'bisect': <module 'bisect' from 'D:\\Python36x64\\lib\\bisect.py'>, '_bisect': <module '_bisect' (built-in)>, '_random': <module '_random' (built-in)>, 'locale': <module 'locale' from 'D:\\Python36x64\\lib\\locale.py'>, 'idlelib.stackviewer': <module 'idlelib.stackviewer' from 'D:\\Python36x64\\lib\\idlelib\\stackviewer.py'>, 'idlelib.debugobj': <module 'idlelib.debugobj' from 'D:\\Python36x64\\lib\\idlelib\\debugobj.py'>, 'idlelib.tree': <module 'idlelib.tree' from 'D:\\Python36x64\\lib\\idlelib\\tree.py'>, 'idlelib.zoomheight': <module 'idlelib.zoomheight' from 'D:\\Python36x64\\lib\\idlelib\\zoomheight.py'>, 'pydoc': <module 'pydoc' from 'D:\\Python36x64\\lib\\pydoc.py'>, 'importlib.util': <module 'importlib.util' from 'D:\\Python36x64\\lib\\importlib\\util.py'>, 'importlib.abc': <module 'importlib.abc' from 'D:\\Python36x64\\lib\\importlib\\abc.py'>, 'contextlib': <module 'contextlib' from 'D:\\Python36x64\\lib\\contextlib.py'>, 'pkgutil': <module 'pkgutil' from 'D:\\Python36x64\\lib\\pkgutil.py'>, 'urllib': <module 'urllib' from 'D:\\Python36x64\\lib\\urllib\\__init__.py'>, 'urllib.parse': <module 'urllib.parse' from 'D:\\Python36x64\\lib\\urllib\\parse.py'>}
['D:\\Python36x64\\Lib\\idlelib', 'D:\\Python36x64\\python36.zip', 'D:\\Python36x64\\DLLs', 'D:\\Python36x64\\lib', 'D:\\Python36x64', 'D:\\Python36x64\\lib\\site-packages']
[<class 'zipimport.zipimporter'>, <function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x000001547224C6A8>]
{'D:\\Python36x64\\python36.zip': None, 'D:\\Python36x64\\DLLs': FileFinder('D:\\Python36x64\\DLLs'), 'D:\\Python36x64\\lib': FileFinder('D:\\Python36x64\\lib'), 'D:\\Python36x64\\lib\\encodings': FileFinder('D:\\Python36x64\\lib\\encodings'), 'D:\\Python36x64': FileFinder('D:\\Python36x64'), 'D:\\Python36x64\\lib\\site-packages': FileFinder('D:\\Python36x64\\lib\\site-packages'), 'D:\\Python36x64\\Lib\\idlelib': FileFinder('D:\\Python36x64\\Lib\\idlelib'), 'D:\\Python36x64\\lib\\idlelib': FileFinder('D:\\Python36x64\\lib\\idlelib'), 'D:\\Python36x64\\lib\\collections': FileFinder('D:\\Python36x64\\lib\\collections'), 'D:\\Python36x64\\lib\\tkinter': FileFinder('D:\\Python36x64\\lib\\tkinter'), 'D:\\Python36x64\\lib\\importlib': FileFinder('D:\\Python36x64\\lib\\importlib'), 'D:\\Python36x64\\lib\\urllib': FileFinder('D:\\Python36x64\\lib\\urllib')}
win32
D:\Python36x64
<built-in function set_asyncgen_hooks>
<built-in function set_coroutine_wrapper>
<built-in function setcheckinterval>
<built-in function setprofile>
<built-in function setrecursionlimit>
<built-in function setswitchinterval>
<built-in function settrace>
<idlelib.run.PseudoOutputFile object at 0x0000015472E33208>
<idlelib.run.PseudoInputFile object at 0x0000015472E331D0>
<idlelib.run.PseudoOutputFile object at 0x0000015472D119E8>
sys.thread_info(name='nt', lock=None, version=None)
3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)]
sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)
[]
3.6
>>> print_all(__builtins__)
		      
<class 'ArithmeticError'>
<class 'AssertionError'>
<class 'AttributeError'>
<class 'BaseException'>
<class 'BlockingIOError'>
<class 'BrokenPipeError'>
<class 'BufferError'>
<class 'BytesWarning'>
<class 'ChildProcessError'>
<class 'ConnectionAbortedError'>
<class 'ConnectionError'>
<class 'ConnectionRefusedError'>
<class 'ConnectionResetError'>
<class 'DeprecationWarning'>
<class 'EOFError'>
Ellipsis
<class 'OSError'>
<class 'Exception'>
False
<class 'FileExistsError'>
<class 'FileNotFoundError'>
<class 'FloatingPointError'>
<class 'FutureWarning'>
<class 'GeneratorExit'>
<class 'OSError'>
<class 'ImportError'>
<class 'ImportWarning'>
<class 'IndentationError'>
<class 'IndexError'>
<class 'InterruptedError'>
<class 'IsADirectoryError'>
<class 'KeyError'>
<class 'KeyboardInterrupt'>
<class 'LookupError'>
<class 'MemoryError'>
<class 'ModuleNotFoundError'>
<class 'NameError'>
None
<class 'NotADirectoryError'>
NotImplemented
<class 'NotImplementedError'>
<class 'OSError'>
<class 'OverflowError'>
<class 'PendingDeprecationWarning'>
<class 'PermissionError'>
<class 'ProcessLookupError'>
<class 'RecursionError'>
<class 'ReferenceError'>
<class 'ResourceWarning'>
<class 'RuntimeError'>
<class 'RuntimeWarning'>
<class 'StopAsyncIteration'>
<class 'StopIteration'>
<class 'SyntaxError'>
<class 'SyntaxWarning'>
<class 'SystemError'>
<class 'SystemExit'>
<class 'TabError'>
<class 'TimeoutError'>
True
<class 'TypeError'>
<class 'UnboundLocalError'>
<class 'UnicodeDecodeError'>
<class 'UnicodeEncodeError'>
<class 'UnicodeError'>
<class 'UnicodeTranslateError'>
<class 'UnicodeWarning'>
<class 'UserWarning'>
<class 'ValueError'>
<class 'Warning'>
<class 'OSError'>
<class 'ZeroDivisionError'>
<built-in method __init_subclass__ of type object at 0x00000000616DCF30>
<built-in function __build_class__>
True
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
<built-in function __import__>
<class '_frozen_importlib.BuiltinImporter'>
builtins

ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)
<built-in function abs>
<built-in function all>
<built-in function any>
<built-in function ascii>
<built-in function bin>
<class 'bool'>
<class 'bytearray'>
<class 'bytes'>
<built-in function callable>
<built-in function chr>
<class 'classmethod'>
<built-in function compile>
<class 'complex'>
Copyright (c) 2001-2017 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
<built-in function delattr>
<class 'dict'>
<built-in function dir>
<built-in function divmod>
<class 'enumerate'>
<built-in function eval>
<built-in function exec>
Use exit() or Ctrl-Z plus Return to exit
<class 'filter'>
<class 'float'>
<built-in function format>
<class 'frozenset'>
<built-in function getattr>
<built-in function globals>
<built-in function hasattr>
<built-in function hash>
Type help() for interactive help, or help(object) for help about object.
<built-in function hex>
<built-in function id>
<built-in function input>
<class 'int'>
<built-in function isinstance>
<built-in function issubclass>
<built-in function iter>
<built-in function len>
Type license() to see the full license text
<class 'list'>
<built-in function locals>
<class 'map'>
<built-in function max>
<class 'memoryview'>
<built-in function min>
<built-in function next>
<class 'object'>
<built-in function oct>
<built-in function open>
<built-in function ord>
<built-in function pow>
<built-in function print>
<class 'property'>
Use quit() or Ctrl-Z plus Return to exit
<class 'range'>
<built-in function repr>
<class 'reversed'>
<built-in function round>
<class 'set'>
<built-in function setattr>
<class 'slice'>
<built-in function sorted>
<class 'staticmethod'>
<class 'str'>
<built-in function sum>
<class 'super'>
<class 'tuple'>
<class 'type'>
<built-in function vars>
<class 'zip'>
>>> print_all('sys')
		      
<method-wrapper '__add__' of str object at 0x0000015472226CE0>
<class 'str'>
<method-wrapper '__contains__' of str object at 0x0000015472226CE0>
<method-wrapper '__delattr__' of str object at 0x0000015472226CE0>
<built-in method __dir__ of str object at 0x0000015472226CE0>
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
<method-wrapper '__eq__' of str object at 0x0000015472226CE0>
<built-in method __format__ of str object at 0x0000015472226CE0>
<method-wrapper '__ge__' of str object at 0x0000015472226CE0>
<method-wrapper '__getattribute__' of str object at 0x0000015472226CE0>
<method-wrapper '__getitem__' of str object at 0x0000015472226CE0>
<built-in method __getnewargs__ of str object at 0x0000015472226CE0>
<method-wrapper '__gt__' of str object at 0x0000015472226CE0>
<method-wrapper '__hash__' of str object at 0x0000015472226CE0>
<method-wrapper '__init__' of str object at 0x0000015472226CE0>
<built-in method __init_subclass__ of type object at 0x00000000616DCF30>
<method-wrapper '__iter__' of str object at 0x0000015472226CE0>
<method-wrapper '__le__' of str object at 0x0000015472226CE0>
<method-wrapper '__len__' of str object at 0x0000015472226CE0>
<method-wrapper '__lt__' of str object at 0x0000015472226CE0>
<method-wrapper '__mod__' of str object at 0x0000015472226CE0>
<method-wrapper '__mul__' of str object at 0x0000015472226CE0>
<method-wrapper '__ne__' of str object at 0x0000015472226CE0>
<built-in method __new__ of type object at 0x00000000616DCF30>
<built-in method __reduce__ of str object at 0x0000015472226CE0>
<built-in method __reduce_ex__ of str object at 0x0000015472226CE0>
<method-wrapper '__repr__' of str object at 0x0000015472226CE0>
<method-wrapper '__rmod__' of str object at 0x0000015472226CE0>
<method-wrapper '__rmul__' of str object at 0x0000015472226CE0>
<method-wrapper '__setattr__' of str object at 0x0000015472226CE0>
<built-in method __sizeof__ of str object at 0x0000015472226CE0>
<method-wrapper '__str__' of str object at 0x0000015472226CE0>
<built-in method __subclasshook__ of type object at 0x00000000616DCF30>
<built-in method capitalize of str object at 0x0000015472226CE0>
<built-in method casefold of str object at 0x0000015472226CE0>
<built-in method center of str object at 0x0000015472226CE0>
<built-in method count of str object at 0x0000015472226CE0>
<built-in method encode of str object at 0x0000015472226CE0>
<built-in method endswith of str object at 0x0000015472226CE0>
<built-in method expandtabs of str object at 0x0000015472226CE0>
<built-in method find of str object at 0x0000015472226CE0>
<built-in method format of str object at 0x0000015472226CE0>
<built-in method format_map of str object at 0x0000015472226CE0>
<built-in method index of str object at 0x0000015472226CE0>
<built-in method isalnum of str object at 0x0000015472226CE0>
<built-in method isalpha of str object at 0x0000015472226CE0>
<built-in method isdecimal of str object at 0x0000015472226CE0>
<built-in method isdigit of str object at 0x0000015472226CE0>
<built-in method isidentifier of str object at 0x0000015472226CE0>
<built-in method islower of str object at 0x0000015472226CE0>
<built-in method isnumeric of str object at 0x0000015472226CE0>
<built-in method isprintable of str object at 0x0000015472226CE0>
<built-in method isspace of str object at 0x0000015472226CE0>
<built-in method istitle of str object at 0x0000015472226CE0>
<built-in method isupper of str object at 0x0000015472226CE0>
<built-in method join of str object at 0x0000015472226CE0>
<built-in method ljust of str object at 0x0000015472226CE0>
<built-in method lower of str object at 0x0000015472226CE0>
<built-in method lstrip of str object at 0x0000015472226CE0>
<built-in method maketrans of type object at 0x00000000616DCF30>
<built-in method partition of str object at 0x0000015472226CE0>
<built-in method replace of str object at 0x0000015472226CE0>
<built-in method rfind of str object at 0x0000015472226CE0>
<built-in method rindex of str object at 0x0000015472226CE0>
<built-in method rjust of str object at 0x0000015472226CE0>
<built-in method rpartition of str object at 0x0000015472226CE0>
<built-in method rsplit of str object at 0x0000015472226CE0>
<built-in method rstrip of str object at 0x0000015472226CE0>
<built-in method split of str object at 0x0000015472226CE0>
<built-in method splitlines of str object at 0x0000015472226CE0>
<built-in method startswith of str object at 0x0000015472226CE0>
<built-in method strip of str object at 0x0000015472226CE0>
<built-in method swapcase of str object at 0x0000015472226CE0>
<built-in method title of str object at 0x0000015472226CE0>
<built-in method translate of str object at 0x0000015472226CE0>
<built-in method upper of str object at 0x0000015472226CE0>
<built-in method zfill of str object at 0x0000015472226CE0>
>>> print_all('__builtins__')
		      
<method-wrapper '__add__' of str object at 0x00000154722411B0>
<class 'str'>
<method-wrapper '__contains__' of str object at 0x00000154722411B0>
<method-wrapper '__delattr__' of str object at 0x00000154722411B0>
<built-in method __dir__ of str object at 0x00000154722411B0>
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
<method-wrapper '__eq__' of str object at 0x00000154722411B0>
<built-in method __format__ of str object at 0x00000154722411B0>
<method-wrapper '__ge__' of str object at 0x00000154722411B0>
<method-wrapper '__getattribute__' of str object at 0x00000154722411B0>
<method-wrapper '__getitem__' of str object at 0x00000154722411B0>
<built-in method __getnewargs__ of str object at 0x00000154722411B0>
<method-wrapper '__gt__' of str object at 0x00000154722411B0>
<method-wrapper '__hash__' of str object at 0x00000154722411B0>
<method-wrapper '__init__' of str object at 0x00000154722411B0>
<built-in method __init_subclass__ of type object at 0x00000000616DCF30>
<method-wrapper '__iter__' of str object at 0x00000154722411B0>
<method-wrapper '__le__' of str object at 0x00000154722411B0>
<method-wrapper '__len__' of str object at 0x00000154722411B0>
<method-wrapper '__lt__' of str object at 0x00000154722411B0>
<method-wrapper '__mod__' of str object at 0x00000154722411B0>
<method-wrapper '__mul__' of str object at 0x00000154722411B0>
<method-wrapper '__ne__' of str object at 0x00000154722411B0>
<built-in method __new__ of type object at 0x00000000616DCF30>
<built-in method __reduce__ of str object at 0x00000154722411B0>
<built-in method __reduce_ex__ of str object at 0x00000154722411B0>
<method-wrapper '__repr__' of str object at 0x00000154722411B0>
<method-wrapper '__rmod__' of str object at 0x00000154722411B0>
<method-wrapper '__rmul__' of str object at 0x00000154722411B0>
<method-wrapper '__setattr__' of str object at 0x00000154722411B0>
<built-in method __sizeof__ of str object at 0x00000154722411B0>
<method-wrapper '__str__' of str object at 0x00000154722411B0>
<built-in method __subclasshook__ of type object at 0x00000000616DCF30>
<built-in method capitalize of str object at 0x00000154722411B0>
<built-in method casefold of str object at 0x00000154722411B0>
<built-in method center of str object at 0x00000154722411B0>
<built-in method count of str object at 0x00000154722411B0>
<built-in method encode of str object at 0x00000154722411B0>
<built-in method endswith of str object at 0x00000154722411B0>
<built-in method expandtabs of str object at 0x00000154722411B0>
<built-in method find of str object at 0x00000154722411B0>
<built-in method format of str object at 0x00000154722411B0>
<built-in method format_map of str object at 0x00000154722411B0>
<built-in method index of str object at 0x00000154722411B0>
<built-in method isalnum of str object at 0x00000154722411B0>
<built-in method isalpha of str object at 0x00000154722411B0>
<built-in method isdecimal of str object at 0x00000154722411B0>
<built-in method isdigit of str object at 0x00000154722411B0>
<built-in method isidentifier of str object at 0x00000154722411B0>
<built-in method islower of str object at 0x00000154722411B0>
<built-in method isnumeric of str object at 0x00000154722411B0>
<built-in method isprintable of str object at 0x00000154722411B0>
<built-in method isspace of str object at 0x00000154722411B0>
<built-in method istitle of str object at 0x00000154722411B0>
<built-in method isupper of str object at 0x00000154722411B0>
<built-in method join of str object at 0x00000154722411B0>
<built-in method ljust of str object at 0x00000154722411B0>
<built-in method lower of str object at 0x00000154722411B0>
<built-in method lstrip of str object at 0x00000154722411B0>
<built-in method maketrans of type object at 0x00000000616DCF30>
<built-in method partition of str object at 0x00000154722411B0>
<built-in method replace of str object at 0x00000154722411B0>
<built-in method rfind of str object at 0x00000154722411B0>
<built-in method rindex of str object at 0x00000154722411B0>
<built-in method rjust of str object at 0x00000154722411B0>
<built-in method rpartition of str object at 0x00000154722411B0>
<built-in method rsplit of str object at 0x00000154722411B0>
<built-in method rstrip of str object at 0x00000154722411B0>
<built-in method split of str object at 0x00000154722411B0>
<built-in method splitlines of str object at 0x00000154722411B0>
<built-in method startswith of str object at 0x00000154722411B0>
<built-in method strip of str object at 0x00000154722411B0>
<built-in method swapcase of str object at 0x00000154722411B0>
<built-in method title of str object at 0x00000154722411B0>
<built-in method translate of str object at 0x00000154722411B0>
<built-in method upper of str object at 0x00000154722411B0>
<built-in method zfill of str object at 0x00000154722411B0>
>>> name_list = dir('__builtins__')
		      
>>> name_list
		      
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> name_list = dir(__builtins__)
		      
>>> name_list
		      
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> name_list[19]
		      
'FileExistsError'
>>> mdo=__builtins__
		      
>>> mdo
		      
<module 'builtins' (built-in)>
>>> getattr(mdo,name_list[19])
		      
<class 'FileExistsError'>
>>> type(getattr(mdo,name_list[19]))
		      
<class 'type'>
>>> type(__builtins__.FileExistsError
	 )
		      
<class 'type'>
>>> __builtins__.FileExistsError.__class__
		      
<class 'type'>
>>> help(help)
		      
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |  
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
 |  
 |  Calling help() at the Python prompt starts an interactive help session.
 |  Calling help(thing) prints help for the python object 'thing'.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

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

>>> help('dir')
		      
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

>>> help('getattr')
		      
Help on built-in function getattr in module builtins:

getattr(...)
    getattr(object, name[, default]) -> value
    
    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.

>>> help(getattr)
		      
Help on built-in function getattr in module builtins:

getattr(...)
    getattr(object, name[, default]) -> value
    
    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.

>>> help('__builtins__.'+name_list[19])
		      
No Python documentation found for '__builtins__.FileExistsError'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help(__builtins__.FileExistsError)
		      
Help on class FileExistsError in module builtins:

class FileExistsError(OSError)
 |  File already exists.
 |  
 |  Method resolution order:
 |      FileExistsError
 |      OSError
 |      Exception
 |      BaseException
 |      object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from OSError:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from OSError:
 |  
 |  characters_written
 |  
 |  errno
 |      POSIX exception code
 |  
 |  filename
 |      exception filename
 |  
 |  filename2
 |      second exception filename
 |  
 |  strerror
 |      exception strerror
 |  
 |  winerror
 |      Win32 exception code
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseException:
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __setstate__(...)
 |  
 |  with_traceback(...)
 |      Exception.with_traceback(tb) --
 |      set self.__traceback__ to tb and return self.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |  
 |  __cause__
 |      exception cause
 |  
 |  __context__
 |      exception context
 |  
 |  __dict__
 |  
 |  __suppress_context__
 |  
 |  __traceback__
 |  
 |  args

>>> help(getattr(__builtins__,name_list[19])
	 )
		      
Help on class FileExistsError in module builtins:

class FileExistsError(OSError)
 |  File already exists.
 |  
 |  Method resolution order:
 |      FileExistsError
 |      OSError
 |      Exception
 |      BaseException
 |      object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from OSError:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from OSError:
 |  
 |  characters_written
 |  
 |  errno
 |      POSIX exception code
 |  
 |  filename
 |      exception filename
 |  
 |  filename2
 |      second exception filename
 |  
 |  strerror
 |      exception strerror
 |  
 |  winerror
 |      Win32 exception code
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseException:
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __setstate__(...)
 |  
 |  with_traceback(...)
 |      Exception.with_traceback(tb) --
 |      set self.__traceback__ to tb and return self.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |  
 |  __cause__
 |      exception cause
 |  
 |  __context__
 |      exception context
 |  
 |  __dict__
 |  
 |  __suppress_context__
 |  
 |  __traceback__
 |  
 |  args

>>> type(SYS)
		      
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    type(SYS)
NameError: name 'SYS' is not defined
>>> type(sys)
		      
<class 'module'>
>>> module('sys')
		      
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    module('sys')
NameError: name 'module' is not defined
>>> dir(__builtins__)
		      
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> [line for line in dir(__builtins__) if 'get' in line]
		      
['getattr']
>>> [line for line in dir(__builtins__) if 'mod' in line]
		      
['divmod']
>>> import pprint
		      
>>> print_all(pprint)
		      
<class 'pprint.PrettyPrinter'>
<class '_io.StringIO'>
['pprint', 'pformat', 'isreadable', 'isrecursive', 'saferepr', 'PrettyPrinter']
{'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'WindowsError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'BufferError': <class 'BufferError'>, 'MemoryError': <class 'MemoryError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-Z plus Return to exit, 'exit': Use exit() or Ctrl-Z plus Return to exit, 'copyright': Copyright (c) 2001-2017 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'license': Type license() to see the full license text, 'help': Type help() for interactive help, or help(object) for help about object., '_': ['divmod']}
D:\Python36x64\lib\__pycache__\pprint.cpython-36.pyc
Support to pretty-print lists, tuples, & dictionaries recursively.

Very simple, but useful, especially in debugging data structures.

Classes
-------

PrettyPrinter()
    Handle pretty-printing operations onto a stream using a configured
    set of formatting parameters.

Functions
---------

pformat()
    Format a Python object into a pretty-printed representation.

pprint()
    Pretty-print a Python object to a stream [default is sys.stdout].

saferepr()
    Generate a 'standard' repr()-like value, but protect against recursive
    data structures.


D:\Python36x64\lib\pprint.py
<_frozen_importlib_external.SourceFileLoader object at 0x0000015472EFD630>
pprint

ModuleSpec(name='pprint', loader=<_frozen_importlib_external.SourceFileLoader object at 0x0000015472EFD630>, origin='D:\\Python36x64\\lib\\pprint.py')
frozenset({<class 'float'>, <class 'complex'>, <class 'NoneType'>, <class 'bytes'>, <class 'bool'>, <class 'str'>, <class 'bytearray'>, <class 'int'>})
<module 'collections' from 'D:\\Python36x64\\lib\\collections\\__init__.py'>
<function _perfcheck at 0x0000015472F09C80>
<function _recursion at 0x0000015472F09BF8>
<class 'pprint._safe_key'>
<function _safe_repr at 0x0000015472F02D08>
<function _safe_tuple at 0x0000015472F02B70>
<module 'sys' (built-in)>
<module 'types' from 'D:\\Python36x64\\lib\\types.py'>
<function _wrap_bytes_repr at 0x0000015472F09D08>
<function isreadable at 0x0000015472F02A60>
<function isrecursive at 0x0000015472F02AE8>
<function pformat at 0x0000015472F028C8>
<function pprint at 0x0000015472F007B8>
<module 're' from 'D:\\Python36x64\\lib\\re.py'>
<function saferepr at 0x0000015472F02510>
>>> 

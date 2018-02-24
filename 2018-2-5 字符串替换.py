Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re,sys,os
>>> #测试Re字符串替换
>>> str1 = r'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
>>> str1
'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
>>> dir(re)
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alphanum_str', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
>>> help(re.sub)
Help on function sub in module re:

sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used.

>>> help(str.replace)
Help on method_descriptor:

replace(...)
    S.replace(old, new[, count]) -> str
    
    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

>>> str1.replace('ADJECTIVE','MMM')
'The MMM panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
>>> str1
'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
>>> #使用str对象的replace方法，只能替换第一个出现的，并形成新的字符串。
>>> 
>>> #下面使用Re替换
>>> re.Sub(r''NOUN','wwwww',str1)
	   
SyntaxError: invalid syntax
>>> re.Sub(r'NOUN','wwwww',str1)
	   
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    re.Sub(r'NOUN','wwwww',str1)
AttributeError: module 're' has no attribute 'Sub'
>>> re.sub(r'NOUN','wwwww',str1)
	   
'The ADJECTIVE panda walked to the wwwww and then VERB. A nearby wwwww was unaffected by these events.'
>>> str1
	   
'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
>>> #使用re的sub
	   
>>> #方法，可以替换所有符合条件的字符，并将生成符合要求的新字符串。
	   
>>> 

Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import webbrowser
>>> import pyperclip
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'
>>> import pyperclip
>>> import requests
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
>>> import requests
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
>>> type(res)
<class 'requests.models.Response'>
>>> res.status_code = requests.codes.ok
>>> res.status_code
200
>>> requests.codes.ok
200
>>> len(res.text)
178981
>>> print(res.text[:250])
﻿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Proje
>>> print(res.text[:2500])
﻿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org/license


Title: Romeo and Juliet

Author: William Shakespeare

Posting Date: May 25, 2012 [EBook #1112]
Release Date: November, 1997  [Etext #1112]

Language: English


*** START OF THIS PROJECT GUTENBERG EBOOK ROMEO AND JULIET ***













*Project Gutenberg is proud to cooperate with The World Library*
in the presentation of The Complete Works of William Shakespeare
for your reading for education and entertainment.  HOWEVER, THIS
IS NEITHER SHAREWARE NOR PUBLIC DOMAIN. . .AND UNDER THE LIBRARY
OF THE FUTURE CONDITIONS OF THIS PRESENTATION. . .NO CHARGES MAY
BE MADE FOR *ANY* ACCESS TO THIS MATERIAL.  YOU ARE ENCOURAGED!!
TO GIVE IT AWAY TO ANYONE YOU LIKE, BUT NO CHARGES ARE ALLOWED!!




The Complete Works of William Shakespeare

The Tragedy of Romeo and Juliet

The Library of the Future Complete Works of William Shakespeare
Library of the Future is a TradeMark (TM) of World Library Inc.


<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM
SHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS
PROVIDED BY PROJECT GUTENBERG ETEXT OF CARNEGIE MELLON UNIVERSITY
WITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE
DISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS
PERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED
COMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY
SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>




1595

THE TRAGEDY OF ROMEO AND JULIET

by William Shakespeare



Dramatis Personae

  Chorus.


  Escalus, Prince of Verona.

  Paris, a young Count, kinsman to the Prince.

  Montague, heads of two houses at variance with each other.

  Capulet, heads of two houses at variance with each other.

  An old Man, of the Capulet family.

  Romeo, son to Montague.

  Tybalt, nephew to Lady Capulet.

  Mercutio, kinsman to the Prince and friend to Romeo.

  Benvolio, nephew to Montague, and friend to Romeo

  Tybalt, nephew to Lady Capulet.

  Friar Laurence, Franciscan.

  Friar John, Franciscan.

  Balthasar, servant to Romeo.

  Abram, servant to Montague.

>>> res_sina = requests.get('http://www.sina.com.cn')
			       
>>> res_sina.status_code == requests.codes.ok
			       
True
>>> len(res_sina)
			       
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    len(res_sina)
TypeError: object of type 'Response' has no len()
>>> type(res_sina)
			       
<class 'requests.models.Response'>
>>> len(res_sina.text)
			       
604596
>>> print(res_sina.text[:1000])
			       
<!DOCTYPE html>
<!-- [ published at 2018-02-09 09:01:16 ] -->
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>æ°æµªé¦é¡µ</title>
	<meta name="keywords" content="æ°æµª,æ°æµªç½,SINA,sina,sina.com.cn,æ°æµªé¦é¡µ,é¨æ·,èµè®¯" />
	<meta name="description" content="æ°æµªç½ä¸ºå¨çç¨æ·24å°æ¶æä¾å¨é¢åæ¶çä¸­æèµè®¯ï¼åå®¹è¦çå½åå¤çªåæ°é»äºä»¶ãä½åèµäºãå¨±ä¹æ¶å°ãäº§ä¸èµè®¯ãå®ç¨ä¿¡æ¯ç­ï¼è®¾ææ°é»ãä½è²ãå¨±ä¹ãè´¢ç»ãç§æãæ¿äº§ãæ±½è½¦ç­30å¤ä¸ªåå®¹é¢éï¼åæ¶å¼è®¾åå®¢ãè§é¢ãè®ºåç­èªç±äºå¨äº¤æµç©ºé´ã" />
    <link rel="mask-icon" sizes="any" href="//www.sina.com.cn/favicon.svg" color="red">
	<meta name="stencil" content="PGLS000022" />
	<meta name="publishid" content="30,131,1" />
	<meta name="verify-v1" content="6HtwmypggdgP1NLw7NOuQBI2TW8+CfkYCoyeB8IDbn8=" />
	<meta name="360-site-v
>>> type(requests.codes)
			       
<class 'requests.structures.LookupDict'>
>>> print(requests.codes)
			       
<lookup 'status_codes'>
>>> help(requests.structures.LooupDict)
			       
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    help(requests.structures.LooupDict)
AttributeError: module 'requests.structures' has no attribute 'LooupDict'
>>> dict(requests.codes)
			       
{}
>>> del res
			       
>>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
			       
>>> res.raise_for_status()
			       
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    res.raise_for_status()
  File "D:\Python36x64\lib\site-packages\requests\models.py", line 935, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
>>> res_sina.raise_for_status()
			       
>>> res_sina.raise_for_status() is None
			       
True
>>> res.raise_for_status() is None
			       
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    res.raise_for_status() is None
  File "D:\Python36x64\lib\site-packages\requests\models.py", line 935, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
			       
>>> res.raise_for_status()
			       
>>> playFile = open('RomeoAndJuliet.txt','wb')
			       
>>> for chunk in res.iter_content(100000):
			       playFile.write(chunk)

			       
100000
78983
>>> playFile.close()
			       
>>> from os import getcwd(),chdir()
			       
SyntaxError: invalid syntax
>>> from os import getcwd,chdir
			       
>>> getcwd()
			       
'D:\\Python36x64\\Lib\\idlelib'
>>> chdir(r'D:\PyScripts')
			       
>>> getcwd()
			       
'D:\\PyScripts'
>>> from os import listdir
			       
>>> listdir()
			       
['2018-2-5 字符串替换.py', 'about', 'AboutBox.zip', 'coinFlip.py', 'dd.zip', 'debug_test.py', 'guess_coin.py', 'logging_test.py', 'mcb', 'mcb2', 'me.zip', 'print_os_walk.py', 'RomeoAndJuliet.txt', 'test.txt', 'zip_dir.py']
>>> 

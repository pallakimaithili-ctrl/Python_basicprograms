Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #INDEXING=positive-start numbering words from 0 ,negative-numbering from n to 0
>>> a="vijayawada"
>>> a[0]
'v'
>>> a[4]
'y'
>>> a[7]+a[8]+a[9]+a[10]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[7]+a[8]+a[9]+a[10]
IndexError: string index out of range
>>> a[6]+a[7]+a[8]+a[9]
'wada'
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]+a[-5]
'vijaya'
>>> #SLICING
>>> #you do the same as indexing regarding numbering
>>> a[0:5]
'vijay'
>>> a[0:6]
'vijaya'
>>> a[-4:-1]
'wad'
>>> a[-4:0]
''
>>> ''
''
>>> a[:4]
'vija'
>>> a[4:]
'yawada'

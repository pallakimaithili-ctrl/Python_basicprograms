Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #STRIDING
>>> #jumping from the first letter to 'c'th letter in [a:b:c] where a=start ; b=end ; c=increment ;
>>> a="Codegnan IT solutions"
>>> b="Vijayawada is a royal city"
>>> a[1:9:1]
'odegnan '
>>> a[::2]
'Cdga Tsltos'
>>> b[1:11:4]
'iaa'
>>> B[::7]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    B[::7]
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> b[::7]
'Vaa '
>>> #works the same for decrement by replacing the -ve numbering with -ve numbering'
>>> a[::-3]
'sil  nd'
>>> b[-2:-6:-7]
't'

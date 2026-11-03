Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #TASK:To set given list in the requested order
>>> a=[9,1,5,2,8,4,7,6,3,0]
>>> 
>>> '''request:[7,6,4,3,0,9,8,5,2,1]'''
'request:[7,6,4,3,0,9,8,5,2,1]'
>>> 
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:]
>>> a2
[4, 7, 6, 3, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> #hence done!🥳

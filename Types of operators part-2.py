Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #TYPES OF OPERATORS @
>>> #2
>>> #Bitwise
>>> #&,|,~,^,>>,<<
>>> a,b=2,4
>>> bin(2)
'0b10'
>>> bin(4)
'0b100'
>>> a&b
0
>>> #& = and
>>> a|b
6
>>> #| = or
>>> a=3
>>> ~a
-4
>>> #~a = -(a+1)
>>> #works for negatives too!
>>> b=-3
>>> ~b
2
>>> a,b=3,6
>>> a^b
5
>>> # ^ -> 0=same bin,1=different bin
>>> #bin = 4 rows '8421'
>>> a,b=12,23
>>> bin(12)
'0b1100'
>>> bin(23)
'0b10111'
>>> a^b
27
>>> a=2
>>> a=2
a<<2
8
bin(2)
'0b10'
#<< = left shift add 'n' zeros to right and 8421 method
a>>3
0
bin(2)
'0b10'
#>> = right shift add'n' zeros to left and 8421 method

#patterns in loops

#right angle triangle
#include <stdio.h>
'''for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()'''
'''
*
* *
* * *
* * * * 
* * * * *
'''
#reverse right angle triangle
'''for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()'''
'''
* * * * *
* * * *
* * *
* *
*
'''
#square
'''for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()'''
'''
* * * *
* * * *
* * * *
* * * *
'''
#pyramid
''''for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()'''
'''
    *
   * *
  * * *
 * * * * 
* * * * *
'''


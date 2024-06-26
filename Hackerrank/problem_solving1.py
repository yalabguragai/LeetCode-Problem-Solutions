# -*- coding: utf-8 -*-
"""Problem Solving1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d2-uNoWqxJM0_fAOa8pZMZbdpaYzQ4cd

# **Hackerrank Problem Solving**

#  1. Compare the Triplets

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.  

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).  

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].    

*   If a[i] > b[i], then Alice is awarded 1 point.
*   If a[i] < b[i], then Bob is awarded 1 point.  
*   If a[i] = b[i], then neither person receives a point.  

Comparison points is the total points a person earned.  

Given a and b, determine their respective comparison points.  

Example  

a = [1, 2, 3]  
b = [3, 2, 1]  
For elements *0*, Bob is awarded a point because a[0] .  
For the equal elements a[1] and b[1], no points are earned.  
Finally, for elements 2, a[2] > b[2] so Alice receives a point.  
The return array is [1, 1] with Alice's score first and Bob's second.   

      Sample Input
    5  6  7   
    3  6  10   
    
    Sample Output 0
    1 1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
    return alice, bob

compareTriplets([5,6,7],[3,6,10])

"""# 2. A Very Big Sum

In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.


    Sample Input
    1000000001 1000000002 1000000003 1000000004 1000000005  

    Output
    5000000015
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    n = len(ar)
    sum = 0
    for i in range(n):
        sum = sum + ar[i]
    return sum

aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005])

"""# 3. Diagnoal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.  

For example, the square matrix  is shown below:  

1  2     3  
4   5   6  
9     8    9    
The left-to-right diagonal = 1+ 5+ 9 =15 . The right to left diagonal = 3+ 5+ 9 = 17. Their absolute difference is |15-17| = 2.


    Sample Input  
    3  
    11  2  4  
    4   5  6  
    10  8 -12  

    Sample Output  
    15
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)

    primarySum = 0
    secondarySum = 0

    for i  in range(n):
        primarySum += arr[i][i]
        secondarySum += arr[i][n-i-1]
    return abs(primarySum - secondarySum)

array = [ [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]]
diagonalDifference(array)

"""# 4. Plus Minus

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.  

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
  
    Sample Input  
    STDIN              Function
    6                 arr[] size n = 6  
    -4 3 -9 0 4 1     arr = [-4, 3, -9, 0, 4, 1]  

    Sample Output  
    0.500000  
    0.333333  
    0.166667  

Explanation
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: 3/6= 0.5000000, negative: 2/6 = 0.333333 and zeros: 1/6 = 0.166667.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_num, negative_num, zero= 0, 0, 0
    x = len(arr)
    for num in range(len(arr)):
        if arr[num] > 0:
            positive_num += 1
        elif arr[num] < 0:
            negative_num += 1
        elif arr[num] == 0:
            zero += 1
    positive = positive_num/x
    negative = negative_num/x
    zeroo = zero/x
    print("{:.6f}".format(positive))
    print("{:.6f}".format(negative))
    print("{:.6f}".format(zeroo))

plusMinus([-4, 3, -9, 0, 4, 1])

"""# 5. Staircase

Staircase detail

    Sample Input
    4
    
    Sample Output
          #
        ##
      ###
    ####

    
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
"""

def staircase(n):
    for i in range(1, n + 1):
            print(" " * (n-i) + "#" * i)

staircase(6)

"""# 6. Min-Max Sum

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.  

Example  
arr = [1,3,5,7,9]

The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24 . The function prints

16 24

    Sample Input

    1 2 3 4 5
    Sample Output

    10 14

Explanation  
The numbers are 1, 2, 3, 4, and 5. Calculate the following sums using four of the five integers:  

Sum everything except 1, the sum is 2+3+4+5= 14.  
Sum everything except 2, the sum is 1+3+4+5= 13.  
Sum everything except 3, the sum is 1+2+4+5= 12.  
Sum everything except 4, the sum is 1+2+3+5= 11.  
Sum everything except 5, the sum is 1+2+3+4= 10.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total = sum(arr)
    sub_list = [0]*len(arr)
    for i in range(len(arr)):
        sub_list[i] = total-arr[i]
    print(min(sub_list), max(sub_list))

miniMaxSum([1,2,3,4,5])

"""# 7. Birthday Cake Candles

You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example  
candles = [4,4,1,3]

The maximum height candles are 4 units high. There are 2 of them, so return 2.

    Sample Input
    3 2 1 3
    Sample Output
    2

Explanation  
Candle heights are [3,2,1,3]. The tallest candles are 3 units, and there are 2 of them.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_number = candles[0]
    count = 1
    for current_number in candles[1:]:
        if current_number > max_number:
            max_number = current_number
            count = 1
        elif current_number == max_number:
            count += 1
    return count

birthdayCakeCandles([3,2,1,3])

"""# 8. Millitary Time Converter

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
*  s= '12:01:00PM'
      Return '12:01:00'.

*  s= '12:01:00AM'
      Return '00:01:00'.

        Sample Input
        07:05:45PM
        
        Sample Output
        19:05:45
"""

def timeConversion(s):
    period = s[-2:]

    # Extract hours, minutes, and seconds as strings
    hh_str = s[:2]
    mm = s[3:5]
    ss = s[6:8]

    # Convert hours from string to integer
    hh = int(hh_str)

    # Convert hours to 24-hour format
    if period == "AM":
        if hh == 12:  # Midnight case
            hh = 0
    else:  # PM case
        if hh != 12:  # Noon case should stay as 12
            hh += 12

    # Format the hours to be two digits without using built-in functions
    hh_24 = f"{hh:02}"

    # Construct the 24-hour format time string
    return f"{hh_24}:{mm}:{ss}"

timeConversion('01:00:01AM')

"""# 9. Grading Students

HackerLand University has the following grading policy:

1.   Every student receives a grade in the inclusive range from  0 to 100.
2.   Any  less than  is a failing grade.

Sam is a professor at the university and likes to round each student's  according to these rules:

  
*   If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.

*   If the value of  is less than 38, no rounding occurs as the result will still be a failing grade.


    Sample Input  
    73  
    67  
    38  
    33

    Sample Output
    75  
    67  
    40  
    33
"""

def gradingStudents(grades):
  upgraded_list = []
  for grade in grades:
    if grade < 38:
      upgraded_list.append(grade)
    else:
      floor_quotient = grade//5
      #diff = (floor_quotient+1)*5 - grades[grade]
      #print([diff])
      next_multiple = (floor_quotient + 1)*5
      if (next_multiple - grade) <3:
       upgraded_list.append(next_multiple)
      else:
        upgraded_list.append(grade)
  return upgraded_list

gradingStudents([73, 67, 38, 33])
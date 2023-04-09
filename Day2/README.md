```lonelyInteger.py``` <br>

Given an array of integers, where all elements but one occur twice, find the unique element.

### Example
a = [1,2,3,4, 3,2,1]

The unique element is 4.

### Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

- int a[n]: an array of integers
### Returns

- int: the element that occurs only once
### Input Format

The first line contains a single integer, , the number of integers in the array.
The second line contains  space-separated integers that describe the values in .


``` diagnolDifference ``` <br>

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

### Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
### Return

int: the absolute diagonal difference
### Input Format

The first line contains a single integer, n, the number of rows and columns in the square matrix .
Each of the next n lines describes a row, arr[i], and consists of  space-separated integers arr[i][j].
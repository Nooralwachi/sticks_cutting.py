# sticks_cutting.py

You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

Write a function that implements stick cutting. It should return an array of integers representing the number of sticks before each cut operation is performed.



Example

Input:     1, 2, 3

Output:  3, 2, 1

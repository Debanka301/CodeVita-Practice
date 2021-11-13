'''
This Question is taken from:- https://www.geeksforgeeks.org/counting-rock-samples-tcs-codevita-2020/

Problem Statement:-

John is a geologist, and he needs to count rock samples in order to send it to a chemical laboratory. 
He has a problem. The laboratory only accepts rock samples by a range of sizes in ppm (parts per million). 
John needs your help. Your task is to develop a program to get the number of rocks in each range accepted by the laboratory.

Problem Statement: Given an array samples[] denoting sizes of rock samples and a 2D array ranges[], 
the task is to count the rock samples that are in the range ranges[i][0] to ranges[i][1], 
for every possible 1 <= i <= N.

Input Format: An positive integer S (the number of rock samples) separated by a blank space, 
and a positive integer R (the number of ranges of the laboratory); 
A list of the sizes of S samples (in ppm), as positive integers separated by space R lines where the ith line containing two positive integers, 
space separated, indicating the minimum size and maximum size respectively of the ith range.

Output Format: R lines where the ith line contains a single non-negative integer indicating the number of the samples which lie in the ith range.

Constraints:

10 <= S <= 10000
1 <= R <= 1000000
1<=size of Sample <= 1000
Example 1

Input: 10 2
345 604 321 433 704 470 808 718 517 811
300 350
400 700
Output: 2 4

Explanation:

There are 10 samples (S) and 2 ranges ( R ). 
The samples are 345, 604,811. The ranges are 300-350 and 400-700. 
There are 2 samples in the first range (345 and 321) and 4 samples in the second range (604, 433, 470, 517). 
Hence the two lines of the output are 2 and 4

Example 2

Input: 20 3
921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195
1 100
50 600
1 1000
Output: 1 12 20

Explanation:

There are 20 samples and 3 ranges. The samples are 921, 107 195. 
The ranges are 1-100, 50-600 and 1-1000. Note that the ranges are overlapping. 
The number of samples in each of the three ranges are 1, 12 and 20 respectively. 
Hence the three lines of the output are 1, 12 and 20.
'''

#Python Code:-
S,R= input("Enter S and R separated by Space:- ").split()
S=int(S)
R=int(R)
arr= list(map(int,input("Enter the numbers:- ").split()))
result=[]
for i in range(R):
    l,h=input("Enter lowest and highest range:- ").split()
    l=int(l)
    h=int(h)
    temp=[]
    for i in range(len(arr)):                               
        if arr[i]>=l and arr[i]<=h:         # If the current element is greater than the lower limit and lesser than the higher limit
            temp.append(arr[i])             # We append it to temp array
    result.append(temp)                     # We pass this temp array for each limits to result array.
    # In this way the result array inturn contains those arrays which have elements based on given limits
for i in range(len(result)):
    print("Final output:- ",len(result[i]),end=" ")           # Printing the length of those individual arrays to get the required output
'''
This Question is taken from:- https://prepinsta.com/tcs-codevita/python-program-for-collecting-candies-problem/

Problem Statement:- 

Question:- Krishna loves candies a lot, so whenever he gets them, he stores them so that he can eat them later whenever he wants to.

He has recently received N boxes of candies each containing Ci candies where Ci represents the total number of candies in the ith box. 
Krishna wants to store them in a single box. The only constraint is that he can choose any two boxes and store their joint contents in an empty box only. 
Assume that there are an infinite number of empty boxes available.

At a time he can pick up any two boxes for transferring and if both the boxes contain X and Y number of candies respectively, then it takes him exactly X+Y seconds of time. 
As he is too eager to collect all of them he has approached you to tell him the minimum time in which all the candies can be collected.

Input Format:

The first line of input is the number of test case T
Each test case is comprised of two inputs
The first input of a test case is the number of boxes N
The second input is N integers delimited by whitespace denoting the number of candies in each box
Output Format: Print minimum time required, in seconds, for each of the test cases. Print each output on a new line.

Constraints:

1 < T < 10
1 < N< 10000
1 < [Candies in each box] < 100009

S.No.	Input	Output
1	1
        4
        1 2 3 4	    19

2	1
        5
        1 2 3 4 5   34

Explanation for sample input-output 1:

4 boxes, each containing 1, 2, 3 and 4 candies respectively.
Adding 1 + 2 in a new box takes 3 seconds.Adding 3 + 3 in a new box takes 6 seconds.
Adding 4 + 6 in a new box takes 10 seconds.Hence total time taken is 19 seconds. 
There could be other combinations also, but overall time does not go below 19 seconds.

Explanation for sample input-output 2:

5 boxes, each containing 1, 2, 3, 4 and 5 candies respectively.
Adding 1 + 2 in a new box takes 3 seconds.Adding 3 + 3 in a new box takes 6 seconds.
Adding 4 + 5 in a new box takes 9 seconds.Adding 9 + 6 in a new box takes 15 seconds.
Hence total time taken is 33 seconds. 
There could be other combinations also, but overall time does not go below 33 seconds.

'''

#Python Code:- 

t=int(input("Enter no. of Test Cases:- "))
for i in range(t):
    n= int(input("Enter no. of elements:- "))
    arr= list(map(int,input("Enter the array:- ").split()))
    cost=[]
    while len(arr)!=1:                                      # While loop will run untill len(arr) becomes 1
        arr.sort()                                          # We are sorting the array
        arr[1]=arr[0]+arr[1]                                # Because of sorting we are sure that the first 2 elements of arr are the two smallest ones. So we add them and store the result in arr[1] only.
        cost.append(arr[1])                                 # In the cost array we append the sum.
        arr=arr[1:]                                         # Next we eliminate the 1st element of array
  
    print("The total time taken is:- ",sum(cost))           # Since the cost array contains indvidual costs,summing up all the costs will give the total cost.
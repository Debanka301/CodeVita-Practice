'''
This Question is taken from:-  https://prepinsta.com/tcs-codevita/minimize-the-sum-problem/

Problem Statement:- 

Given an array of integers, perform atmost K operations so that the sum of elements of final array is minimum. An operation is defined as follows –

Consider any 1 element from the array, arr[i].
Replace arr[i] by floor(arr[i]/2).
Perform next operations on the updated array.
The task is to minimize the sum after utmost K operations.
Constraints

1 <= N
K <= 10^5.
Input

First line contains two integers N and K representing size of array and maximum numbers of operations that can be performed on the array respectively.
Second line contains N space separated integers denoting the elements of the array, arr.
Output

Print a single integer denoting the minimum sum of the final array.
Input

4 3

20 7 5 4

Output

17

Explanation

Operation 1 -> Select 20. Replace it by 10. New array = [10, 7, 5, 4]
Operation 2 -> Select 10. Replace it by 5. New array = [5, 7, 5, 4].
Operation 3 -> Select 7. Replace it by 3. New array = [5,3,5,4].
Sum = 17.

'''
#Python Code:- 

N,K= input("Enter N and K separated by Space:- ").split()
N=int(N)
K= int(K)
arr= list(map(int,input("Enter the array:- ").split()))
for i in range(K):
    arr.sort(reverse=True)                 # The array is Sorte to ensure the 0th element is always the largest one.
    arr[0]=arr[0]//2                       # We make arr[0]//2 because doing floor division of the largest elent will ensure the sum of the arr to be lowest.
print("The present array:- ",arr)
print("The minimizd Sum:- ",sum(arr))
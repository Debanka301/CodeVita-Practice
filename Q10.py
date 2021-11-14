'''
This Question is taken from:-  https://prepinsta.com/tcs-codevita/python-program-to-solve-the-divine-divisor-problem/

Problem Statement:- 

Question -: Print a line containing all the divisors in increasing order separated by space.

Input Format: The first line of input contains an integer ‘N’ denoting the number.

Output Format: Print a line containing all the divisors in increasing order separated by space.

Constraints:
1 <= N <= 10^8

S.no	Input	Output	 
1	    10	    1 2 5 10

'''
#Python Code:-

n= int(input("Enter the number:- "))
arr=[]
for i in range(1,n+1):
    if n%i==0:
        arr.append(i)
arr.sort()
print("All the divisors of ",n," in ascending order are:- ",arr)
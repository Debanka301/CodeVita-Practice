'''
This Question is taken from:- https://www.geeksforgeeks.org/philaland-coin-tcs-mockvita-2020/
Problem Statement:-
The problem solvers have found a new Island for coding and named it as Philaland. 
These smart people were given a task to make purchase of items at the Island easier by distributing various coins with different value. 
Manish has come up with a solution that if we make coins category starting from $1 till the maximum price of item present on Island, then we can purchase any item easily. 
He added following example to prove his point. 

Lets suppose the maximum price of an item is 5$ then we can make coins of {$1, $2, $3, $4, $5} to purchase any item ranging from $1 till $5.
Now Manisha, being a keen observer suggested that we could actually minimize the number of coins required and gave following distribution {$1, $2, $3}. 
According to him any item can be purchased one time ranging from $1 to $5. 
Everyone was impressed with both of them.

Your task is to help Manisha come up with minimum number of denominations for any arbitrary max price in Philaland.

Input: N = 10
Output: 4
Explanation:
According to Manish {$1, $2, $3, … $10} must be distributed.
But as per Manisha only {$1, $2, $3, $4} coins are enough to purchase any item ranging from $1 to $10. 
Hence minimum is 4. Likewise denominations could also be {$1, $2, $3, $5}. Hence answer is still 4.

Input: N = 5
Output: 3
Explanation:
According to Manish {$1, $2, $3, $4, $5} must be distributed.
But as per Manisha only {$1, $2, $3} coins are enough to purchase any item ranging from $1 to $5. 
Hence minimum is 3. Likewise denominations could also be {$1, $2, $4}. Hence answer is still 3.


Approach:-

Every number can be represented as power of two:-
For N = 12, 
If we choose the denominations as {1, 2, 4, 8}
Then every number up to 12 can be represented as –

1 ==> 1
2 ==> 2
3 ==> 2 + 1
4 ==> 4
5 ==> 4 + 1
6 ==> 4 + 2
7 ==> 4 + 2 + 1
8 ==> 8
9 ==> 8 + 1
10 ==> 8 + 2
11 ==> 8 + 2 + 1
12 ==> 8 + 4

In this question we run a while loop and divide the n value untill it becomes less than 1 and we increment the count
which was initially zero.
We finally print count value for each Test case.
'''


#Python Code:-

t=int(input("Enter no. of Test-cases:- "))
values =[]
for i in range(t):
    N=int(input("Enter N:- "))
    values.append(N)
for i in values:
    count = 0
    while i>=1:
        i=i//2
        count=count+1
    print("Result:- ",count)
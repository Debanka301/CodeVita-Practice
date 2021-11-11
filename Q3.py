'''
This question has been taken from ;- https://prepinsta.com/tcs-codevita/c-code-for-consecutive-prime-sum/

Question – :  Some prime numbers can be expressed as a sum of other consecutive prime numbers.

For example
5 = 2 + 3,
17 = 2 + 3 + 5 + 7,
41 = 2 + 3 + 5 + 7 + 11 + 13.
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Constraints: 2<N<=12,000,000,000

S.no	Input	Output	Comment
1	     20	      2	(Below 20 there are two such members; 5 and 17) 5=2+3 17=2+3+65+7
2	     15	      1

'''
#Python code:-

def PrimeChecker(a):       #Funtion to check prime number
    if a > 1:    
        for j in range(2, int(a/2) + 1):    
            if (a % j) == 0:  
                return False  
        else:  
            return True    
    else:  
        return False

n=int(input("Enter n:- "))  # N value is taken as input
Sum=0
l=[]
S=[]
result=[]
for i in range(2,n+1):
    if(PrimeChecker(i)==True):  # If any value between 2 and N is prime we are inserting it in array l and doing the sum
        l.append(i)             # of that element and the element before and storing it in array S
        Sum=Sum+i               # In this way we are obtaining sums of all the consecutive prime numbers from 2 to N.
        S.append(Sum)
for i in S:
    if(PrimeChecker(i) and i<=n):  # Next we are checking in the array S that which sums are prime and fall within N
        result.append(i)           # We then append those values to array result
result=result[1:]                  # We eliminate the first element which is 2 as it got included due to for loop
print("The resultant array:- ",result)                      # This result array contains sums of consecutive prime numbers which fall within 0 to N.
print("The no. of prime numbers which are sums of consecutive prime numbers in range 0 to",n,"is :- ",len(result))



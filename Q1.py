''' This Question has been taken from:- http://www.theinsightcoders.com/Codevita/CodevitaStatement01.html

Codevita Problem 1 - Lexi Strings
Statement
Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?

You are given a string P that denotes the new order of the letters in the English dictionary.

You need to print the smallest lexicographic string made from the given string S.

Constraints
1 <= T <= 1000
Length(P) = 26
1 <= length(S) <= 100
All character in the string S, P are in lower case

Input Format
The first line contains number of test cases T
The second line has the string P
The third line has the string S

Output Format
Print single string in a new line for every test case giving the result.

Example:

Input
2
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezvxbintma
ativedoc

Output
bdca
codevita

Python Code:- 
'''
n=int(input("No.of Test cases:- ")) 
p=[]
s=[]
for i in range(n):
  strinp=str(input("Enter P:- "))
  p.append(strinp)
  strins=str(input("Enter S:- "))
  s.append(strins)
result=[]
for i in range(len(p)):
  pr=[k for k in p[i]]
  sr=s[i]
  inde=[]
  for j in sr:
    inde.append(pr.index(j))
  inde.sort()
  new=[]
  for i in inde:
    new.append(pr[i])
  res="".join(new)
  result.append(res)
print("--------------------------------")
print("Result:- ")
for i in result:
  print(i)





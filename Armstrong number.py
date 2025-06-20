#Armstrong number
n=int(input())
s=len(str(n))
original=n
rem=0
new=0
i=0

while n>0:
    rem=n%10
    rem=rem**s
    new+=rem
    n//=10
    i+=1
# print(new)
if new==original:
    print("Armstrong number") 
else:
    print("not armstrong")  


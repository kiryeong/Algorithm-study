import sys
sys.stdin=open("input.txt","rt")
n=int(input())
a=list(map(int, input().split()))
'''
def digit_sum(x):
    while x>0:
        sum=0
        sum+=x%10
        x=x//10
    return sum
'''
def digit_sum(x):
    sum=0
    for i in str(x):     
        sum+=int(i)
    return sum

max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)
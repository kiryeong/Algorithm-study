import sys
sys.stdin=open("input.txt","rt")
n=int(input())
a=list(map(int,input().split()))
ave=round((sum(a)/n)+0.5) # 파이썬에서의 round는 rount_half_even 방식을 택한다. ex) 4.5면 4로 간다. 
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print("%d %d" %(ave, res))
    


    

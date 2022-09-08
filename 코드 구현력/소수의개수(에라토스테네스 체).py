import sys
sys.stdin=open("input.txt","rt")
n = int(input())
# 에라토스테네스 체
ch=[0]*(n+1)
print(ch)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)

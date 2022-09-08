import sys
sys.stdin=open("input.txt","rt")
n, k = map(int, input().split())
a=list(map(int, input().split()))
res=set() # set은 중복을 없애주는 자료구조 
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res) # set을 List 구조로 바꿔줘야함
res.sort(reverse=True) #내림차순
print(res[k-1])
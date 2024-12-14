n = int(input())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
steps=0
while min(arr1)>-1:
    m=min(arr1)

    for i in range(n):
        if arr1[i]!=m:
            arr1[i]=arr1[i]-arr2[i]
            steps =steps+1
    if len(set(arr1))==1:
        print(steps)
        break
else:
    print(-1)
  
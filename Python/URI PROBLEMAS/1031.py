from collections import deque
def jos(k, j):
    if k == 1:
        return 0
    else:
        return (jos(k-1, j) + j) % k + 1

    d = deque(k)
    while len(d) > 1:
        d.rotate(-j)
        d.pop()
    return(d.pop())


n = int(input())
for i in range(n):
    [k, j] = input().split()
    k = int(k)
    k = [x for x in range(1, int(k)+1)]
    j = int(j)
    result = jos(k, j)
    print('Case %d: %d'%(i+1, result))
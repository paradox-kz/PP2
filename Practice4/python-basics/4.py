def fun(max):
    cnt = 0
    while cnt <= max:
        yield cnt
        cnt += 12


n = int(input())
ctr = fun(n)

for num in ctr:
    print(num,end=' ')
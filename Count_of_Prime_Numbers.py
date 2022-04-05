import time

t1 = time.time()


def prime_num(n):
    for i in range(n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                yield i


c = 0
for i in prime_num(100):
    c += 1

print(c)

t2 = time.time() - t1

print(t2)

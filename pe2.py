fib = lambda x:1 if x<2 else fib(x-1) + fib(x-2)
print(sum(filter(lambda x:x if x<4000000 else 0, map(fib, [x for x in range(2, 33, 3)]))))

print(filter(lambda x:not sum([x%i==0 for i in range(2,x)]),filter(lambda x:x!=0,[x if 600851475143%x == 0 else 0 for x in range(2, int(600851475143**0.5))]))[-1])

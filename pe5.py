a = 2*3*5*7*11*13*17*19

for i in range(a,999999999999,a):
	if i%4==0 and i%6==0 and i%8==0 and i%9==0 and i%10==0 and i%12==0 and i%14==0 and i%15==0 and i%16==0 and i%18==0 and i%20==0:
		print i
		break
		
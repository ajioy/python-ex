def fib(n):
	a, b = 0, 1
	while a < b:
		print(a, end=' ')
		a, b = b, a+b
		print()


fib(1000)
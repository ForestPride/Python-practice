def main():
	x = eval(input("type an integer: "))
	y = 1
	for i in range(x):
		y = y * (i+1)
		print(y)

main()

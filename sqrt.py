# A very inefficient square root calculator.
# Takes a numerical input and calculates a close suare root by guess and check.

def main():
	print("Slow square root calculator!")
	x = float(input("type an integer here: "))
	guess = x/2
	while (round(guess**2,3)/x != 1): 
		if guess**2 > x:
			guess = guess - 0.0001
			print(guess)
		elif guess**2 < x:
			guess = guess + 0.0001
			print(guess)
	print(guess)
main()

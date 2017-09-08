# File: chaos.py
# A simple program illustrating chaotic behavior.

print("This is a chaotic function.")

x = eval(input("type a number between 0 and 1: "))
y = eval(input("type another number between 0 and 1: "))

print("X   ""\ty   ")
print("*" * 20)
for i in range(10):
    x = 3.9 * x * (1 - x)
    y = 3.9 * y * (1 - x)
    print("{0:0.3f}\t{1:0.3f}" .format(x, y))

def fib(n):
    old = 0
    new = 1
    for i in range(n):
        original = new
        new = new+old
        old = original
        """
        print("old:", old)
        print("cur:", new)
        print(new)
        """
    return new

def main():
    n = eval(input("Enter an integer for the nth fibonacci number: "))
    print(fib(n))
main()

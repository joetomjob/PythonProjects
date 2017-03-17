def fib(n):
    if n==1 or n==0:
        return 1,1
    else:
        f2,calls2 = fib(n - 2)
        f1, calls1 = fib(n - 1)
        return f2+f1,calls1+calls2+1


def main():
    print(fib(8))
if __name__=='__main__':
    main()
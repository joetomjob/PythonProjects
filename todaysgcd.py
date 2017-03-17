__author__ = 'zjb'

def gcd(a,b):
    '''
    :param a: a number
    :param b: the other number
    :return: gcd(a,b) AND number of calls required
    '''
    if b == 0:
        return a, 1
    else:
        interim, steps = gcd(b, a % b)
        return interim, steps + 1

'''
result = gcd(15,21)
print(gcd(17406,2108))
print(gcd(2132131245986678986,345784579879184537))
'''

def fib(n):
    '''
    :param n:
    :return: fib number and number of calls
    '''
    if n == 0 or n == 1:
        return 1, 1
    else:
        f2, calls2 = fib(n-2)
        f1, calls1 = fib(n-1)
        return f2+f1, calls2+calls1+1

print(fib(4))
print(fib(33))


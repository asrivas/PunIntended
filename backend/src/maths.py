"""
implement some math functions
this might be more fun to write in haskell
"""

# lambda passed to reduce
mult = lambda x, y: x * y


# TODO boolean indicating primality. use sieve method
def is_prime(n):
    return False


# TODO probabilistic primality test. look up the algo.
def is_prime_p(n):
    return False


# TODO greatest common denominator
def gcd(a, b):
    return 1


# relative primeness
def rel_prime(a, b):
    return gcd(a,b) == 1


# TODO return string indicating prime factorization of n
# 15 -> "2^0 * 3^1 * 5^1"
# 12 -> "2^2 * 3^1"
def prime_factorization(n):
    return ""


# TODO symbolic differentiation
# this could def be a haskell function
# easy to define the expr datatype
# but wed have to define a canonical string formatting of expressions
# for user input
def derivative(expr):
    return None


# return n!
# use xrange for O(1) space
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(mult, xrange(1,n+1))


def choose(n, k):
    return factorial(n) / (factorial(k) * (factorial(n - k)))


# i suspect this version is faster
# but requires floating math, should be tested carefully
# specifically, fails for choose(13,6)
def choose2(n, k):
    return int(reduce(mult, [((n - (k - i)) * 1.0 / i) for i in xrange(1,k+1)]))



# a few simple tests, nothing serious
def simple_tests():
    print factorial(4)
    print choose(9,2)
    print choose2(9, 2)

    for n in xrange(1,100):
        for k in xrange(1, n+1):
            print "n: %d, k: %d" % (n, k)
            print choose(n, k)
            print choose2(n, k)
            assert(choose(n, k) == choose2(n, k))

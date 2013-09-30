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


# http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.94.1384&rep=rep1&type=pdf
# fast determinisitic primality testing based on the above paper
def is_prime_fast(n):
    # check if n is a power other than a first power using newton iteration
    # if it is, return false
    
    # let D = ceil(log(n) ^2)
    # find a period system (r1,q1), (r2,q2), ..., (rk, qk) for n
    # with d:= q1q2...qk >= D and d = O(D)
    
    # let B = floor(sqrt(d) log(n)) 
    # see if n has a prime factor in [1,B]
    
    # attempt to find a monic polynomial f in (Z/nZ)[x] of degree d
    
    # for integers a, 1 <= a <= b, check if (x+a)^n is congruent to x^n + a (mod n, f(x))
    # if a congruence fails, declare n composite. otherwise, n is prime
    return False


# http://en.wikipedia.org/wiki/Adleman%E2%80%93Pomerance%E2%80%93Rumely_primality_test
def is_prime_cyclotopy(n):
    return False


# greatest common divisor using euclid method
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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

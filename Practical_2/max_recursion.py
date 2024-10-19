import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1050)
print(sys.getrecursionlimit())


print(sys.argv)

def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n-1, sum+n)

c = 999
print(recursive_function(c, 0))
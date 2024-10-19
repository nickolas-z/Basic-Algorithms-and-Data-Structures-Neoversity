def fibo(n, a, b):
 
    if (n > 0):
 
        # Function call
        fibo(n - 1, b, a + b)
 
        # Print the result
        print(a, end=" ")
 
 
if __name__ == "__main__":
 
    N = 10
    fibo(N, 0, 1)
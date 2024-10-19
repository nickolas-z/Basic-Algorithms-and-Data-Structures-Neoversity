import random
import timeit

# Generate random prices for testing
prices = [random.randint(1, 10000) for _ in range(10)]
prices = [100, 80, 50, 60, 40, 80, 100, 50]

def calculate_span_two_stacks(price):
    n = len(price)
    s1 = []
    s2 = []
    ans = []
    for i in range(n):
        while(s1 != [] and price[s1[-1]] < price[i]):
            s1.pop()

        if(s1 == []):
            ans.append(i+1)
        else:
            ans.append(i - s1[-1])

        s1.append(i)
        s2.append(price[i])

    return ans

# Function to calculate span using stack
def calculate_span(prices):
    n = len(prices)
    stack = []
    spans = [0] * n

    for i in range(n):
        print(stack)
        while stack and prices[stack[-1]] < prices[i]:
            stack.pop()
        
        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return spans

# Function to calculate span without using stack
def calculate_span_without_stack(price):
    n = len(price)
    S = [None] * n
    S[0] = 1
    for i in range(1, n, 1):
        S[i] = 1
        j = i - 1
        while (j >= 0) and (price[i] > price[j]):
            S[i] += 1
            j -= 1
    return S


# Measuring time for approach with two stacks
print(calculate_span_two_stacks(prices))
two_stacks_time = timeit.timeit(lambda: calculate_span_two_stacks(prices), number=1)

print("Time taken with two stacks approach:", two_stacks_time)


# Measuring time for stack approach
print(calculate_span(prices))
stack_time = timeit.timeit(lambda: calculate_span(prices), number=5)

# Measuring time for approach without using stack
print(calculate_span_without_stack(prices))
no_stack_time = timeit.timeit(lambda: calculate_span_without_stack(prices), number=5)

print("Time taken with stack approach:", stack_time)
print("Time taken without stack approach:", no_stack_time)

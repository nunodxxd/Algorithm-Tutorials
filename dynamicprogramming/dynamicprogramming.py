# Dynamic programming (example with Fibonacci algorithm )

def fib(n):
    # Create an array to store the calculated values
    fib_values = [0, 1]
    for i in range(2, n+1):
        # Calculate the next value based on the previous two
        next_value = fib_values[i-1] + fib_values[i-2]
        # Store the value in the array
        fib_values.append(next_value)
    return fib_values[n]

# fast
print(fib(10))
# fast
print(fib(100))
# fast
print(fib(100000))


#############################################################
# Without Dynamic programming 
# Example of a recursive function 
# As the input size grows, 
# the number of recalculations grows exponentially, 
# making this function very slow for large inputs.


def fib2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

# fast
print(fib2(10))
# How about we go for coffee?
print(fib2(100))
# not in this life 
print(fib2(10000))
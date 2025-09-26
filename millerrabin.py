import random

# Function to check if n is a prime using Miller-Rabin
def is_prime(n, k=5):
    """
    Miller-Rabin Primality Test
    n : number to test
    k : number of rounds (more rounds = more accuracy)
    """

    # Handle small cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:  # even numbers greater than 2 are not prime
        return False

    # Step 1: Write n-1 as (2^r) * d, with d odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Step 2: Repeat k times
    for _ in range(k):
        a = random.randint(2, n - 2)  # random base
        x = pow(a, d, n)  # compute a^d % n

        if x == 1 or x == n - 1:
            continue  # this round passes

        # Square x repeatedly
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # composite

    return True  # probably prime


# --- Example usage ---
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is probably prime")
else:
    print(f"{num} is composite")

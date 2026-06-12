"""
Palindromic Divisors

Problem: Find all divisors of a number that are palindromic.
A palindromic number reads the same forwards and backwards.
"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]


def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def find_palindromic_divisors(n):
    palindromic_divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and is_palindrome(i):
            palindromic_divisors.append(i)
    return palindromic_divisors


def find_palindromic_divisors_optimized(n):
    import math
    palindromic_divisors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # i is a divisor
            if is_palindrome(i):
                palindromic_divisors.append(i)
            
            j = n // i
            if j != i and is_palindrome(j):
                palindromic_divisors.append(j)
    
    return sorted(palindromic_divisors)



# Test


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    
    print(f"\nNumber: {n}")
    print("-" * 40)
    
    all_divisors = find_divisors(n)
    print(f"All divisors: {all_divisors}")
    
    palindromic = find_palindromic_divisors(n)
    print(f"Palindromic divisors: {palindromic}")
    
    palindromic_optimized = find_palindromic_divisors_optimized(n)
    print(f"Palindromic divisors (optimized): {palindromic_optimized}")
    
    print("\n" + "-" * 40)
    print("Checking each divisor:")
    for d in all_divisors:
        if is_palindrome(d):
            print(f"✓ {d} → palindromic")
        else:
            print(f"✗ {d} → not palindromic")
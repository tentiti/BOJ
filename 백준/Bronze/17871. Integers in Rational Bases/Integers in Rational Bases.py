def base_pq_expansion(p, q, n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = []
    
    while n > 0:
        remainder = n % p
        result.append(digits[remainder])
        n = (n - remainder) * q // p
    
    return ''.join(result[::-1]) if result else '0'

# Read input
p, q, n = map(int, input().split())

# Calculate and print the result
print(base_pq_expansion(p, q, n))
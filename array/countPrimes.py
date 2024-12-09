def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 10
primes = []
for i in range(2, n + 1):
    if is_prime(i):
        primes.append(i)

print(primes)  # Output: [2, 3, 5, 7]
print(len(primes))  # Output: 4


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        # Create a boolean array to mark prime numbers
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime

        # Start marking non-prime numbers
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i as non-prime
                for j in range(i * i, n, i):  # Start from i^2
                    is_prime[j] = False

        # Count the number of True values in the array
        return sum(is_prime)

# Example usage
solution = Solution()
result = solution.countPrimes(1000000)  # Count primes below 1,000,000
print(result)  # Efficient and avoids TLE

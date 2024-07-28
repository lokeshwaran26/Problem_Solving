class UserMainCode(object):
    @classmethod
    def eqSplit(cls, A, N):
        def product_of_array(arr):
            result = 1
            for num in arr:
                if num == 0:
                    return 0
                result *= num
            return result

        def find_divisors(n):
            divisors = set()
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
            return divisors

        total_product = product_of_array(A)
        if total_product == 0:
            return -1

        divisors = find_divisors(total_product)
        max_parts = -1

        for divisor in divisors:
            current_product = 1
            parts = 0
            for num in A:
                current_product *= num
                if current_product == divisor:
                    parts += 1
                    current_product = 1
                elif current_product > divisor:
                    break
            if current_product == 1:
                max_parts = max(max_parts, parts)

        return max_parts if max_parts >= 2 else -1
    
obj = UserMainCode()
A = [2,2,4,4,2,2]

print(obj.eqSplit(A, 5))

# Function to read input and invoke eqSplit





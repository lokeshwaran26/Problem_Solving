def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_kth_glowing_bulb(switches, K):
    # Step 1: Identify prime indices from 1 to 40
    prime_indices = [i for i in range(1, 41) if is_prime(i)]

    # Step 2: Find which prime-indexed switches are ON
    on_prime_switches = [i for i in prime_indices if switches[i - 1] == '1']

    # Step 3: Identify all glowing bulbs
    glowing_bulbs = set()
    for switch in on_prime_switches:
        multiple = switch
        while multiple <= 100000:  # Considering bulbs in a large range, adjust as needed
            glowing_bulbs.add(multiple)
            multiple += switch

    # Step 4: Sort the glowing bulbs and find the Kth one
    sorted_glowing_bulbs = sorted(glowing_bulbs)
    return sorted_glowing_bulbs[K - 1] if K <= len(sorted_glowing_bulbs) else -1


# Input
switches = "0110000000000000000000000000000000000000"
K = 7

# Convert switch input to list of integers
switches_list = list(switches)

# Find the Kth glowing bulb
result = find_kth_glowing_bulb(switches_list, K)
print(result)  # Output should be 10

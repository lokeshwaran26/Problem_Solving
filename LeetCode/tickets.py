# Time Needed to Buy Tickets


# Example 1:

# Input: tickets = [2, 3, 2], k = 2
# Output: 6
# Explanation:
# - In the first pass , everyone in the line buys a ticket and the line becomes [1, 2, 1].
# - In the second pass , everyone in the line buys a ticket and the line becomes [0, 1, 0].
# The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
# Example 2:

# Input: tickets = [5, 1, 1, 1], k = 0
# Output: 8
# Explanation:
# - In the first pass , everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
# - In the next 4 passes, only the person in position 0 is buying tickets.
# The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0

        for i, x in enumerate(tickets):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total

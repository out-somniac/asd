# Given donominations of coins and a target amound of N.
# What is the minimum possible number of coins to used.
# Example: [1, 2, 5], N = 11 -> 5 + 5 + 1 -> answear: 3


def count_ways(N, allowed):
    F = [float('inf') for i in range(N + 1)] # F[i] denotes minimum number of coins to have value of i
    F[0] = 0
    for i in range(N + 1):
        for number in allowed:
            if i - number < N:
                F[i] = min(F[i], F[i - number] + 1)
    return F[N]

if __name__ == "__main__":
    print(count_ways(11, [1, 2, 5]))
    print(count_ways(6, [1, 3, 4]))
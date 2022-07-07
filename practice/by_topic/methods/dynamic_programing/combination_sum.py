# Given the target value N and an array of allowed numbers, 
# count ways to write N as the sum of those numbers

def count_ways(N, allowed):
    F = [0 for i in range(N+1)] # F[i] denotes in how many ways can we write a number i as a sum of allowed nums
    F[0] = 1 # For example sum 0 can be writen in only one way
    for i in range(N+1):
        for number in allowed:
            if number + i < N + 1:
                F[number + i] += F[i] # We can write sum (number + i) in howewer namy ways we could write F[i] + sth
    return F[N]



if __name__ == "__main__":
    allowed = [1, 2, 3]
    N = 17
    print(count_ways(N, allowed))
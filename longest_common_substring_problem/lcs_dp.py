def compute_lcs(S1, S2):
    # build a 2D array where dp[k][j] represents
    # the length of lcs of S1[0:j] and S2[0:k]
    dp = build_dp(S1, S2)

    print(dp)    
    # construct lcs from dp
    elems = construct_lcs(dp, S1, S2)

    return ''.join(reversed(elems))


def build_dp(m, n):
    m = len(S1)
    n = len(S2)
    dp = [[0] * m for i in range(n)]
    for k in range(n):
        for j in range(m):
            if S1[j] == S2[k]:
                dp[k][j] = dp[k-1][j-1] + 1
            else:
                dp[k][j] = max(dp[k-1][j], dp[k][j-1])
    return dp


def construct_lcs(dp, S1, S2):
    j = len(S1) - 1
    k = len(S2) - 1

    elems = []
    while dp[k][j] > 0:
        if dp[k][j] == 1 + dp[k-1][j-1]:
            elems.append(S1[j])
            k -= 1
            j -= 1
        elif dp[k-1][j] >= dp[k][j-1]:
            k -= 1
        else:
            j -= 1 
    return elems

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S1 = input()
        S2 = input()
        lcs = compute_lcs(S1, S2)
        print("Case: #{}: {}".format(str(i), lcs))

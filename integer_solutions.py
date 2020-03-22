from dedupe import dedupe


def compute_integer_solutions(N, K):
    if N < 2:
        S = list()
        for i in range(K):
            s = [0] * K
            s[i] = 1
            S.append(s)
        return S

    S = compute_integer_solutions(N-1, K)

    A = merge_one(S)

    return A


def merge_one(S):
    A = list()
    for s in S:
        for j in range(K):
            a = list(s)
            a[j] += 1
            A.append(a)
    return A
    

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = [int(s) for s in input().split(" ")]
        r = compute_integer_solutions(N, K)
        dedupe_r = dedupe(r)
        print(dedupe_r)
    

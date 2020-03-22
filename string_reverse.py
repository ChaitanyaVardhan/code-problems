import time


def compute_reverse(S):
    if len(S) < 2:
        return S
    
    mid = len(S) // 2
    L = S[0:mid]
    R = S[mid:len(S)]
    comp_l = compute_reverse(L)
    comp_r = compute_reverse(R)
    A = [comp_r, comp_l]
    rev = ''.join(A)
    return rev
    
if __name__ == "__main__":
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    for i in range(len(S)):
        start = time.time()
        rev = compute_reverse(S[i])
        end = time.time()
        print(f"Time taken for length: {len(S[i])}: {end-start}")
        print(rev)

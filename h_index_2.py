import time


def compute_h_index(S):
    result = []
    for i in range(1, len(S)+1):
        h = compute_h_index_for_set(S[0:i])
        result.append(h)

    return result


def compute_h_index_for_set(X):
    citation_arr = [0] * len(X)
    for x in X:
        if x < len(X):
            citation_arr[x-1] += 1
        else:
            citation_arr[len(X)-1] += 1
            
    score_arr = [0] * len(X)
    score_arr[len(X)-1] = citation_arr[len(X)-1]
    l = len(X) - 2
    while l >= 0:
        score_arr[l] = citation_arr[l] + score_arr[l+1]
        l -= 1

    h_index = 0
    for l in range(len(X)):
        if score_arr[l] >= l + 1:
            h_index = l + 1

    return h_index


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        S = [None] * N
        S = [int(i) for i in input().split(" ")]
        start = time.time()
        result = compute_h_index(S)
        end = time.time()
        print("Case #{}: {}".format(t+1, ' '.join(str(h) for h in result)))
        print(f"Time for input size {N}: {end-start}")

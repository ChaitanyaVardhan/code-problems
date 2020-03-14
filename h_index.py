# Input: Line 1 gives the total number of test cases T in the file
# T test cases follow. For each test case, line 1 gives the number of
# research papers. Line 2 gives the citations for each paper separated
# by a space
# Sample input:
#2
#5
#4 3 3 2 3
#10
#2 1 4 4 8 10 5 4 6 8

import time


def compute_h_index(S):
    h_index_list = []
    for i in range(1, len(S)+1):
        a = 0
        j = i
        while a < j:
            a = get_max_count(j, S[0:i])
            j -= 1
        h_index_list.append(a)
    return h_index_list


def get_max_count(i, arr):
    count = 0
    for j in range(len(arr)):
        if arr[j] >= i:
            count += 1
    return count


if __name__ == "__main__":
    T = int(input())
    for n in range(T):
        N = int(input())
        S = [int(s) for s in input().split(" ")]
        start = time.time()
        result = compute_h_index(S)
        end = time.time()
        print("Case #{}: {}".format(str(n+1), ' '.join(str(i) for i in result)))
        print(f"Time taken {end-start}")

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
    for _ in range(T):
        N = int(input())
        S = [int(s) for s in input().split(" ")]
        result = compute_h_index(S)
        print(result)

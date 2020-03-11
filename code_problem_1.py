# input: line 1 gives the count of strings to follow
# N lines follow where each line has 1 string

def shortest_encapsulator(S):
    if len(S) == 1:
        return S[0]

    result = []
    result.append(S[0])
    for k in range(1, len(S)):
        i = 0
        l = len(S[k])
        candidates = []
        for i in range(l):
            candidates.append(S[k][0:l - i])

        j = 0
        while j < len(candidates):
            if candidates[j] ==''.join(result)[-len(candidates[j]):]:
                break
            else:
                j += 1
        if j < len(candidates):
            result.append(S[k][len(candidates[j]):])

    final_str = ''.join(result)
    return final_str


if __name__ == "__main__":
    S = []
    count = int(input())
    for _ in range(count):
        S.append(input())

    expected_out = "abracadabracad"
    se = shortest_encapsulator(S)
    print(f"output string: {se}")
    print(f"Expected Output : {expected_out}")
    if expected_out == se:
        print("Passed")
    else:
        print("Failed")
    

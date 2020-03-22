def dedupe(S):
    if len(S) < 2:
        return S
    
    if len(S) < 3:
        R = []
        if S[0] != S[1]:
            R.append(S[0])
            R.append(S[1])
        else:
            R.append(S[0])
        return R

    mid = len(S) // 2
    S1 = S[0:mid]
    S2 = S[mid:len(S)]
    R1 = dedupe(S1)
    R2 = dedupe(S2)
    R = []
    merge(R1, R2, R)
    
    return R


def merge(S1, S2, R):
    i = j = 0
    while i < len(S1) and j < len(S2):
        if S1[i] != S2[j]:
            R.append(S1[i])
            i += 1
        else:
            R.append(S2[j])
            i += 1	
            j += 1
    if i == len(S1):
        while j < len(S2):
            R.append(S2[j])
            j += 1
    else:
        while i < len(S1):
            R.append(S1[i])
            i += 1

    return R


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        S = [int(s) for s in input().split()]
        R = dedupe(S)
        print(S)
        print(R)

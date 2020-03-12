def lcs(S):
    if len(S) < 2:
        return S[0]
    
    s1 = S[0]
    s2 = S[1]
    result = []
    i = 0
    pos = -1
    while i < len(s1) and pos < len(s2):
        new_pos = get_pos(s1[i], s2[pos + 1:])
        print(i, new_pos, pos)
        if new_pos >= 0:
            pos = pos + new_pos + 1
            result.append(s1[i])
        i += 1
        
    lcs_str = ''.join(result)
    return lcs_str

def get_pos(c, target_str):
    pos = -1
    i = 0
    while i < len(target_str):
        if target_str[i] == c:
            pos = i
            break
        else:
            i += 1
    return pos


if __name__ == "__main__":
    S = []
    count = int(input())
    for _ in range(count):
        S.append(input())

    print(f"input strings: {S}")
    s = lcs(S)
    print(f"lcs: {s}")


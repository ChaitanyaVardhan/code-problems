def lcs(S):
    if len(S) < 2:
        return S[0]

    candidate_strs = [S[0][i:] for i in range(len(S[0]))]
    lcs_strs = []
    s2 = S[1]
    for s1 in candidate_strs:
        s = get_lcs(s1, s2)
        lcs_strs.append(s)

    lcs = get_global_lcs(lcs_strs)
    return lcs


def get_lcs(s1, s2):
    result = []
    i = 0
    pos = -1
    while i < len(s1) and pos < len(s2):
        new_pos = get_pos(s1[i], s2[pos + 1:])

        if new_pos >= 0:
            pos = pos + new_pos + 1
            result.append(s1[i])
        i += 1
        
    lcs_str = ''.join(result)
    return lcs_str


def get_global_lcs(lcs_strs):
    i = 0
    max_len = 0
    max_idx = 0
    while i < len(lcs_strs):
        if len(lcs_strs[i]) > max_len:
            max_len = len(lcs_strs[i])
            max_idx = i
        i += 1
        
    return lcs_strs[max_idx]


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

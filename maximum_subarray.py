def compute_max_subarr(S):
    if len(S) < 2:
        return S

    mid = len(S) // 2
    S1 = S[0:mid]
    S2 = S[mid:len(S)]
    R1 = compute_max_subarr(S1)
    R2 = compute_max_subarr(S2)
    
    R = []
    mid_s1 = mid_s2 = False
    if S1[-1] == R1[-1]:
        mid_s1 =  True
    if S2[0] ==  R2[0]:
        mid_s2 = True

    merge_max_subarr(R1, R2, R, mid_s1, mid_s2)

    # correct for missing middle elements
    if not mid_s1 or not mid_s2:
        i = j = 0
        while i < len(S1):
            if S1[i] == R1[-1]:
                break
            else:
                i += 1
        while j < len(S2):
            if S2[j] == R2[0]:
                break
            else:
                j += 1
        if not mid_s1 and not mid_s2:
            total_sum = sum(R1) + sum(S1[i+1:]) + sum(S2[0:j]) +sum(R2)
            if total_sum >= max(sum(R1), sum(R2)):
                R = []
                R.extend(R1)
                R.extend(S1[i+1:])
                R.extend(S2[0:j])
                R.extend(R2)                
        elif not mid_s1:
            total_sum = sum(R1) + sum(S1[i+1:]) + sum(R2)
            if total_sum >= max(sum(R1), sum(R2)):
                R = []
                R.extend(R1)
                R.extend(S1[i+1:])
                R.extend(R2)                
        elif not mid_s2:
            total_sum = sum(R1) + sum(S2[0:j]) + sum(R2)
            if total_sum >= max(sum(R1), sum(R2)):
                R = []
                R.extend(R1)
                R.extend(S2[0:j])
                R.extend(R2)
    
    return R


def merge_max_subarr(R1, R2, R, mid_s1, mid_s2):
    if mid_s1 and mid_s2:
        if sum(R1) > 0 and sum(R2) > 0:
            R.extend(R1)
            R.extend(R2)
        elif sum(R1) > sum(R2):
            R.extend(R1)
        else:
            R.extend(R2)
        return R
        
    if sum(R1) > sum(R2):
        R.extend(R1)
    else:
        R.extend(R2)
    return R

    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        l = input()
        S = []
        for a in l.split(" "):
            S.append(int(a))
        R = compute_max_subarr(S)
        print("Case #{}: {}".format(str(i+1), R))

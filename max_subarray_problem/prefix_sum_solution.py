def solve(S):
    #compute prefix sum array of S[a:len(S)]
    # and select max prefix sum    
    cand_arr = []
    for a in range(len(S)):
        ans_dict = select_max_prefix_sum(S, a)
        cand_arr.append(ans_dict)

    # find max sum value cand_arr
    max = cand_arr[0]["max"]
    a = 0
    b = cand_arr[0]["end_index"] + 1
    for j in range(1, len(cand_arr)):
        if cand_arr[j]["max"] > max:
            max = cand_arr[j]["max"]
            a = j
            b = cand_arr[0]["end_index"] + 1

    return dict(
        sum=max,
        a=a,
        b=b
    )
            
    
def select_max_prefix_sum(S, a):
    print(a)
    print(S)
    prefix_sum_S = []
    prefix_sum_S.append(S[a])
    max = prefix_sum_S[0]
    end_index = a
    for i in range(a+1, len(S)):
        prefix_sum_S.append(prefix_sum_S[i-1] + S[i])
        if prefix_sum_S[i] >= max:
            max = prefix_sum_S[i]
            end_index = i

    print(prefix_sum_S)
    return dict(
        max=max,
        end_index=end_index
    )


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S = [int(s) for s in input().split()]
        # Subarray S[a:b] with sum
        ans_dict = solve(S)
        print(f"Case #{i}: {ans_dict['sum']}, {ans_dict['a']}, {ans_dict['b']}")
        
        


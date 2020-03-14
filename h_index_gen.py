import sys
import random

if __name__ == "__main__":
    T = int(input())
    n_arr = []
    
    print(T)
    
    for _ in range(T):
        n_arr.append(int(input()))
        
    for N in n_arr:
        int_arr = []
        for j in range(N):
            i = random.randint(1, N)
            int_arr.append(i)
        print(N)
        print("{}".format(' '.join(str(i) for i in int_arr)))


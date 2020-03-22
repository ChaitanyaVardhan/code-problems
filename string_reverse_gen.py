import string
import random


if __name__ == "__main__":
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    print(len(S))
    for i in range(len(S)):
        len = int(S[i])
        A = [random.choice(string.ascii_letters) for j in range(len)]
        print(''.join(A))

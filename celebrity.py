# Find the celebrity from a list of N persons attending the party
# using a method f(a, b) that returns True if person a knows b.
# The celebrity does not know anybody. So, in this case the method f
# always returns False.
# This should be done in O(N) time and the method f takes O(1) time
import random
import time

def find_celebrity(N, C):
    party_attendees = [i for i in range(N+1)]
    celebrity = party_attendees[0]
    for i in range(1, len(party_attendees)):
        if knows(party_attendees[i], celebrity):
            continue
        else:
            celebrity = party_attendees[i]

    return celebrity


def knows(a, b):
    if a == b:
        return True
    elif b == C:
        return True
    elif a == C:
        return False
    else:
        return bool(random.randint(0,1))

    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        l = input().split(" ")
        N = int(l[0])
        global C
        C = int(l[1])
        start = time.time()
        r = find_celebrity(N, C)
        end = time.time()
        print("Case: #{}: {}".format(str(i+1), str(r)))
        print("Time for Case: #{}: {}".format(str(i+1), str(end-start)))

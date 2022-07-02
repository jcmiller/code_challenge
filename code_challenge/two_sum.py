seen = dict()

test = [1,2,3,4]

def solution(target=3, test=test):
    for i, x in enumerate(test):
        if target-x in seen:
            return seen[target-x], i
        seen[x] = i
    return -1, -1

print(solution(3, test))


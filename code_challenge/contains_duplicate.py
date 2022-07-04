from typing import List
def contain_duplicate(input: List[int]) -> bool:
    i = 0
    j = i+1
    while i < len(input) - 1:
        while j < len(input):
            if input[i] == input[j]:
                return True
            j+=1
        i+=1
        j=i+1
    return False


assert(contain_duplicate([1,2,3,3]) == True)
assert(contain_duplicate([1,2,3,4]) == False)
assert(contain_duplicate([]) == False)
assert(contain_duplicate([-5]) == False)
assert(contain_duplicate([1,1]) == True)


def contain_duplicate_set(input: List[int]) -> bool:
    seen = set()
    for i in input:
        if i in seen:
            return True
        seen.add(i)
    return False


assert(contain_duplicate_set([1,2,3,3]) == True)
assert(contain_duplicate_set([1,2,3,4]) == False)
assert(contain_duplicate_set([]) == False)
assert(contain_duplicate_set([-5]) == False)
assert(contain_duplicate_set([1,1]) == True)
# FUNCTION TO RETURN MAXIMUM ELEMENT
# USING RECURSION

def findMaxRec(S, n):
    # if n = 0 means whole array
    # has been traversed
    if (n == 1):
        return S[0]
    return max(S[n -1], findMaxRec(S, n-1))

# DRIVER CODE
if __name__ =="__main__":
    S = [5, 8, 10, 12, -3, 15, 20]
    n = len(S)
    print(findMaxRec(S,n))

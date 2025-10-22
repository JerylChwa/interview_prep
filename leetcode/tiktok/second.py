"""
Find longest decreasing subsequence
"""

def FindLongestDecreasingSubsequence(input):
    """
    At each element, we can either, 
    decide to add it to our current subsequence
    skip this element
    or start a new subarray starting from this element
    once i == len(input), we have finished processing all the elements
    if len of our subarray is greater than the longest subarray, we can update longest, and update our result
    """
    longest = [0]
    res = None

    def dfs(i, curarray):
        nonlocal res
        if i == len(input):
            if len(curarray) > longest[0]:
                longest[0] = len(curarray)
                res = curarray[:]
            return 

        if curarray:
            last_element = curarray[-1]
            if input[i] < last_element:
                dfs(i+1, curarray+[input[i]])
        
        dfs(i+1, curarray) # skips current element
        dfs(i+1, [input[i]]) # start new subarray
    
    dfs(0, [])
    return res

# print(FindLongestDecreasingSubsequence([1,2,6,5,4,3,2,1]))


"""
Find number of envelopes that can fit in each other
[1,3],
[1,6],
[2,7]
"""

def FindMaxEnvelopesFit(input):
    input.sort(key=lambda x : (-1*x[0], -1*x[1]))
    longest = [0]
    res = None

    def dfs(i, curarray):
        nonlocal res
        if i == len(input):
            if len(curarray) > longest[0]:
                longest[0] = len(curarray)
                res = curarray[:]
            return 

        if curarray:
            last_element = curarray[-1]
            if input[i][0] < last_element[0] and input[i][1] < last_element[1]:
                dfs(i+1, curarray+[input[i]])
        
        dfs(i+1, curarray) # skips current element
        dfs(i+1, [input[i]]) # start new subarray
    
    dfs(0, [])
    print(res)
    return len(res)

print(FindMaxEnvelopesFit([[1,6], [6,1], [5,4], [6,4], [6,7], [2,3]]))


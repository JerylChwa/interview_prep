"""
A greedy algorithm is an algorithm that repeatedly makes the locally optimal choice at each step, returning a globally optimum solution.

Pattern:

Maintaining ordering -> Monotonic stack

"""




class Greedy:

    """
        Given a string s, 
        remove duplicate letters so that every letter appears only once
        Return the subsequence with the smallest lexico ordering.
        A subsequence is a string that can be derived from another string by deleting any or none of the characters.
    """
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Since we want to return the subsequence with the smallest ordering, the intuition is to maintain a monotonically increasing stack
        Greedily choose and maintain the subsequence with the smallest lexico ordering

        However, this is tricky as if we look at this sample input
        bcab

        The subsequence is bca, but we just maintain the textbook monotonically increasing stack, we will get ab.
        Look at element c. Notice that c will not appear in any positions on the right handside.
        So even though a is lexically smaller than c, we have to keep c at the top of the stack as this is the only position it will appear

        We can keep first do a one pass to calculate total frequency to determine if a letter still has any more appearances further down the string.
        Now, our algo returns subsequence bcab
        Notice the repeated b, we also need to keep track if the letter has already been greedily processed. So we need to maintain a visited set.
        """

        visited = set()
        count = [0]*26 # for 26 letters
        stack = []

        # one pass to count freq
        for letter in s:
            count[ord(letter)-ord('a')] += 1

        for letter in s:
            count[ord(letter)-ord('a')] -= 1
            if letter in visited: # skip if letter has been already greedily processed
                continue
            # check if stack non empty
            # check if current letter lexically greater than top of stack
            # check if letter at top of stack still appears on rhs
            # if all these is true then pop
            while stack and letter < stack[-1] and count[ord(stack[-1])-ord('a')] > 0:                                    
                visited.remove(stack.pop())

            stack.append(letter)
            visited.add(letter)

        
        return ''.join(stack)
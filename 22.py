"""
[Medium]

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

def solution(words, s):
    # Only way I can think about doing this is recursively looking through the list for the first string that matches the beginning of the string.
    # The problem is that let's assume we have 'the' and 'thetan' but not 'tan'. Then, if we match 'the' when the example contains 'thetan', we will return null. So we need to match the maximal elements first.
    # To do that, we just sort the list such that things like 'thetan' precede 'the'.
    words = sorted(words)[::-1]
    def find_first(st, result):
        isnull = True
        if st == '':
            return result
        else:
            for word in words:
                if st.startswith(word):
                    return find_first(st[len(word):], result+[word])
                    isnull = False
                    break
            if isnull:
                return None
    return find_first(s, [])

print(solution(['bed', 'bath', 'and', 'beyond', 'bedbath'], "bedbathandbeyond"))

"""
[Hard]
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

"""
Okay, this is pretty hard.
Let's think.

s = nixjkjxivj
How do I go about solving this? I guess I start from the beginning and count the number of each character that occurs. and I stop when I reach k for one. We don't need it to go through the whole list necessarily, because if we already have a substring that is as long as the remaining characters, we can stop.

How should we do this? We should define a function that recursively strips off the "checking" letter of the string, compare that to the k condition, and if we're good, we continue to the next letter and so on.

We're going to need to keep track of the unique characters, the highest count, and the current count of the substring. It should stop when the remaining substring is as long as the current highest count.
"""
def sol():
    def func(s, k, high=0):
        if len(s) <= high:
            return high
        else:
            substring = ""
            count = 0
            uniques = set()
            for c in s:
                if len(uniques.union({c}))<=k:
                    count += 1
                    uniques.add(c)
                else:
                    break
            if high < count:
                high = count
            return func(s[1:], k, high)
    print(func("acccccbfca", 2, 0))

sol()

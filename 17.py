"""
[Hard]
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""

"""
Okay what's the strategy here. First, we're looking for files, which are terminal nodes (leafs).

Since this is a tree structure, we could convert the string to a tree data structure. But this could be costly. So let's assume that we want to extract this information only through operations on the string.

When we find terminal nodes we want to traverse back up the tree to the root. We can do that by checking the number of tabs following new lines.

Assume that a file nodes is prefixed with "/n/t/t/t" like file2.ext above. What we want to do is then find the immediate node on the right prefixed with one fewer /t. Then look leftward from there for one fewer /t and so on until we reach the root.

We then splice this together. We do this for each file and keep track of the longest file path.
"""
import re

def solution(s):
    # First we need to find all of the files.
    fnpattern = '\\n((?:\\t)*)([a-zA-Z0-9]*\.[a-z0-9]+)'
    files = re.finditer(fnpattern, s)
    high = 0
    for f in files:
        fname = f.group(2)
        n = f.group(1).count('\t')
        fpath = find_last(s[:f.start()], n-1, "")
        path_len = len(fpath+f.group(2))
        if high < path_len:
            high = path_len
    return high

def find_last(s2, n, fpath):
    if n == 0:
        pattern = "^(.*?)(\\n|$)"
        root = re.search(pattern, s2)
        return root.group(1)+"/"+fpath
    else:
        pattern = '\\n(?:\\t){'+str(n)+'}(\S*?)$'
        folder_obj = re.search(pattern, s2)
        fpath = folder_obj.group(1)+"/"+fpath
        return find_last(s2[:folder_obj.start()], n-1, fpath)

print(solution("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

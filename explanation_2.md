# Problem 2: File Recursion

## Reason
Since the structure of a directory is like a tree, it's suitable to use recursive here to traverse all sub folders all the way the deepest level. Therefore, we can easily check all levels of folder and files to see if they end with the given suffix

## Efficiency

- Time complexity  
  O(n * m): n is the depth of the given directory, m is the average number of folders in each level of the directory

- Space complexity  
  O(n): n is the depth of the given folder

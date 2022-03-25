# Problem 4: Active Directory

## Reason
Since we need to check all possible subfolders under the group, here use Recursion to traverse all levels of group and check if the user is valid. So here will check if the name is the same as group name, and then will check all subgroup names to see if it matches.

## Efficiency

- Time complexity
  - O(m*n), where m is the depth of the directory structure, and n is the number of users

- Space complexity
  - O(m*n), where m is the depth of the directory, n is the number of users

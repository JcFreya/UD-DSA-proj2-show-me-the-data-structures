'''
# Problem 4: Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by str representing their ids.
Write a function that provides an efficient look up of whether the user is in a group.
'''

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == group.get_name():
        return True

    if user in group.get_users():
        return True

    for group in group.get_groups():
        return is_user_in_group(user, group)
    return False


print('----------Test1----------')
print(is_user_in_group("sub_child_user", parent))   # True

print('----------Test2----------')
print(is_user_in_group("other_group_user", child))  # False

print('----------Test3----------')
print(is_user_in_group("subchild", parent)) # True

print('----------Test4----------')
print(is_user_in_group("", parent)) # False

print('----------Test5----------')
print(is_user_in_group(None, parent))   # False

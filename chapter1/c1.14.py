# 对不原生支持比较操作的对象排序

class user:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [user(23), user(99), user(3)]
temp = sorted(users, key=lambda u: u.user_id)
print(temp)

from operator import attrgetter

sorted(users, key=attrgetter('user_id'))

from WebApi import Teacher
import random

t = Teacher()
t.login()
choose_username = random.sample(t.list_teacher()[0], 1)[0]
total_1 = t.list_teacher()[1]
print('现有username:')
print(t.list_teacher())
print('随机选取已存在的username为 ' + choose_username)
assert t.add_teacher(choose_username)['retcode'] == 1
total_2 = t.list_teacher()[1]
assert total_1 == total_2
print('-------pass-------')

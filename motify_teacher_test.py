from WebApi import Teacher
import random

t = Teacher()
t.login()
list_id = t.list_teacher()[2]
choose_id = random.sample(list_id, 1)[0]
print('随机选择id：' + str(choose_id))
username = input('输入用户名')
res = t.modify_teacher(choose_id, username)
assert res['retcode'] == 0
assert username in t.list_teacher()[0]
print('-----pass------')

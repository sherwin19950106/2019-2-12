from WebApi import Teacher
import random

t =Teacher()
t.login()
list_id = t.list_teacher()[2]
total_1 = t.list_teacher()[1]
choose_id = random.sample(list_id,1)[0]
print('随机选取的删除id为：' + str(choose_id))
assert t.delete_teacher(choose_id)['retcode'] == 0
total_2 = t.list_teacher()[1]
assert total_1 -1 == total_2
assert choose_id not in t.list_teacher()[2]
print('-----pass-----')

from WebApi import Teacher
import random, time


def test_add():
    t = Teacher()
    t.login()
    choose_username = random.sample(t.list_teacher()[0], 1)[0]
    total_1 = t.list_teacher()[1]
    print('现有username:')
    print(t.list_teacher()[0])
    print('随机选取已存在的username为 ' + choose_username)
    assert t.add_teacher(choose_username)['retcode'] == 1
    total_2 = t.list_teacher()[1]
    assert total_1 == total_2


def test_motify():
    t = Teacher()
    t.login()
    list_id = t.list_teacher()[2]
    choose_id = random.sample(list_id, 1)[0]
    print('随机选择id：' + str(choose_id))
    username = str(time.time())
    res = t.modify_teacher(choose_id, username)
    assert res['retcode'] == 0
    list_name = t.list_teacher()[0]
    assert username in list_name


def test_delete():
    t = Teacher()
    t.login()
    list_id = t.list_teacher()[2]
    total_1 = t.list_teacher()[1]
    choose_id = random.sample(list_id, 1)[0]
    print('随机选取的删除id为：' + str(choose_id))
    assert t.delete_teacher(choose_id)['retcode'] == 0
    total_2 = t.list_teacher()[1]
    assert total_1 - 1 == total_2
    assert choose_id not in t.list_teacher()[2]



import requests,pprint,random

class first_api():
    def login(self):
        url = 'http://localhost/api/mgr/loginReq'
        datas = {
            'username': 'auto',
            'password': 'sdfsdfsdf'

        }
        res = requests.post(url, data=datas)
        assert res.json()['retcode'] == 0
        self.dic = {'sessionid': res.cookies['sessionid']}
        return res.json()

class Course(first_api):
    def delete_course(self, id):
        url = 'http://localhost/api/mgr/sq_mgr/'
        datas = {
            'action': 'delete_course',
            'id': id
        }
        res = requests.delete(url, data=datas, cookies=self.dic)
        assert res.json()['retcode'] == 0
        return id

    def list_course(self):
        url = 'http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
        res = requests.get(url, cookies=self.dic)
        assert res.json()['retcode'] == 0
        list_id = []
        for i in res.json()['retlist']:
            list_id.append(i['id'])
        return res.json(), list_id, res.json()['total']


class Teacher(first_api):
    def list_teacher(self):
        url = 'http://localhost/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20'
        res = requests.get(url,cookies=self.dic)
        assert res.json()['retcode'] == 0
        list_username = []
        list_id = []
        for i in res.json()['retlist']:
            list_username.append(i['username'])
            list_id.append(i['id'])
        return list_username,res.json()['total'],list_id

    def add_teacher(self, username):
        url = 'http://localhost/api/mgr/sq_mgr/'
        datas = {
            'action': 'add_teacher',
            'data': '''{
    "username":"%s",
    "password":"123456",
    "realname":"真实姓名",
    "desc":"细节描述",
    "courses":[],
    "display_idx":1
} ''' % (username,)}
        res = requests.post(url, data=datas, cookies=self.dic)
        print(res.json())
        return res.json()

    def modify_teacher(self, id, username):
        if username in self.list_teacher()[0]:
            print('登录名修改重复')
            print('------fail------')
        else:
            url = "http://localhost/api/mgr/sq_mgr/"
            payload = {
                    'action':'modify_teacher',
                    'id': id,
                    'newdata': '''
                    {
        "username":"%s",
        "password":"password",
        "realname":"真实姓名",
        "desc":"细节描述",
        "courses":[],
        "display_idx":1
    }
                    ''' % (username,)
            }
            response = requests.put(url, data=payload, cookies=self.dic)
            return response.json()

    def delete_teacher(self, id):
        url = "http://localhost/api/mgr/sq_mgr/"
        payload = {
            'action':'delete_teacher',
            'id':id
        }
        response = requests.delete( url, data=payload, cookies=self.dic)
        return response.json()







import json
from flask import make_response
from random import randint

class crud:
    def __init__(self) -> None:
        u=open('users.json')
        self.data=json.load(u)
        u.close()

    def getAll(self):
        return self.data

    def getOne(self,id):
        users=self.data['users']
        for user in users:
            if user['id']==id:
                return json.dumps(user)

    def postOne(self,user):
        user=json.dumps(user)
        id=randint(0,100)
        user['id']=id
        users=self.data['users']
        print(users)
        users.append(user)
        self.data['users']=users
        return 'User save'

    def putOne():
        pass
    def deleteOne():
        pass

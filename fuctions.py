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
        return False

    def postOne(self,user):
        id=randint(0,100)
        users=self.data['users']
        users.append({
            "id":id,
            "nombre":user["nombre"],
            "edad":user["edad"],
            "pais":user["pais"]
        })
        self.data['users']=users
        return 'User save'

    def putOne(self,id,user):
        user=self.getOne(id)
        if user is False:
            return 'User dont exist'
        users=self.data['users']
        for u in users:
            if u['id']==id:
                u=user
        self.data['users']=users
        return 'User update'
        
    def deleteOne(self,id,user):
        user=self.getOne(id)
        if user is False:
            return 'User dont exist'
        users=self.data['users']
        for u in users:
            if u['id']==id:
                users.remove(u)
        self.data['users']=users
        return 'User delete'

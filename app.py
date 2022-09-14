from flask import Flask, request,jsonify
from users import users

users=users()
app=Flask(__name__)

@app.route('/users/')
def getAll():
    return users.getAll()

@app.route('/users/<int:id>')
def getUser(id):
    return users.getOne(id)

@app.route('/users/',methods=['POST'])
def newUser():
    user=request.json
    return users.postOne(user)

@app.route('/users/<int:id>', methods=['PUT'])
def updateUser(id):
    user=request.json
    return users.putOne(id,user)

@app.route('/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    return users.deleteOne(id)
    
#####################OTHER WAY#############################
# @app.route('/users/',methods=['GET','POST'])
# def getPost():
#     if request.method=='GET':
#         return users.getAll()
#     user=request.json
#     return users.postOne(user)
# @app.route('/users/<int:id>',methods=['GET','DELETE','PUT'])
# def getDelPut(id):
#     if request.method=='GET':
#         return users.getOne(id)
#     if request.method=='PUT':
#         user=request.json
#         return users.putOne(id,user)
#     else:
#         return users.deleteOne(id)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request,jsonify
from fuctions import crud

crud=crud()
app=Flask(__name__)

@app.route('/users/')
def getAll():
    return crud.getAll()

@app.route('/users/<int:id>')
def getUser(id):
    return crud.getOne(id)

@app.route('/users/',methods=['POST'])
def newUser():
    user=request.json
    return crud.postOne(user)

@app.route('/users/<int:id>', methods=['PUT'])
def updateUser(id):
    user=request.json
    return crud.putOne(id,user)

@app.route('/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    user=request.json
    return crud.deleteOne(id,user)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
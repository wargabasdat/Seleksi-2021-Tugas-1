from app import app
from app.controller import apicontroller


@app.route('/')
def hello():
    return "anjayy"


@app.route('/api/v1/imdb', methods=['GET'])
def getall():
    return apicontroller.getall()


@app.route('/api/v1/imdb/<id>', methods=['GET'])
def getsingle(id):
    return apicontroller.getsingle(id)

@app.route('/api/v1/imdb/title/<title>', methods=['GET'])
def getsinglebytitle(title):
    return apicontroller.getsinglebytitle(title)

@app.route('/api/v1/imdb', methods=['POST'])
def createdata():
    return apicontroller.createdata()

@app.route('/api/v1/imdb/<id>', methods=['DELETE'])
def deletedata(id):
    return apicontroller.deletedata(id)

@app.route('/api/v1/imdb/<id>', methods=['PUT'])
def updatedata(id):
    return apicontroller.updatedata(id)


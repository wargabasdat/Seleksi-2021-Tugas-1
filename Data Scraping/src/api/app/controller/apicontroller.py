from flask import jsonify, make_response, Response, request
from app import app
import pymongo
from bson import json_util
from bson.objectid import ObjectId

db = pymongo.MongoClient(
    "mongodb+srv://dwibagus154:mUnvBeu7vR3hAaK@cluster0.uqmyh.mongodb.net/test?retryWrites=true&w=majority")
# database
mydatabase = db["scraping"]
# collection
collection = mydatabase['imdb']


def getall():
    data = collection.find()
    response = json_util.dumps(data)
    return Response(response, mimetype='application/json')


def getsingle(id):
    data = collection.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(data)
    return Response(response, mimetype='application/json')


def getsinglebytitle(title):
    data = collection.find_one({'title': title})
    response = json_util.dumps(data)
    return Response(response, mimetype='application/json')


def createdata():
    title = request.form.get('title')
    description = request.form.get('description')
    rating = request.form.get('rating')
    genre = request.form.get('genre')
    time = request.form.get('time')
    certificate = request.form.get('certificate')

    id = collection.insert({
        'title': title,
        'description': description,
        'rating': rating,
        'genre': genre,
        'time': time,
        'certificate': certificate
    })

    return make_response(jsonify({
        'massage': 'data created'
    })), 200


def deletedata(id):
    collection.delete_one({'_id': ObjectId(id)})
    return make_response(jsonify({
        'massage': 'data deleted'
    })), 200


def updatedata(id):
    title = request.form.get('title')
    description = request.form.get('description')
    rating = request.form.get('rating')
    genre = request.form.get('genre')
    time = request.form.get('time')
    certificate = request.form.get('certificate')

    collection.update_one({
        '_id': ObjectId(id)}, {
            '$set': {
                'title': title,
                'description': description,
                'rating': rating,
                'genre': genre,
                'time': time,
                'certificate': certificate
            }})

    return make_response(jsonify({
        'massage': 'data updated'
    })), 200

from dotenv import load_dotenv
from bson.json_util import dumps
import pymongo
import os
import json
import glob


load_dotenv()
server = os.getenv("SERVER_URL")
client = pymongo.MongoClient(server)
db = client["basdat"]
col = db["jobs"]

db.jobs.drop()
for f in glob.glob("../data/*_job.json"):
    file = open(f,)
    data = json.load(file)
    col.insert_one(data)

col = db['jobs'].find({})
doc_count = db['jobs'].count_documents({})

with open("../../Data Storing/export/collection.json", "w") as file:
    file.write('[')
    # Start from one as type_documents_count also starts from 1.
    for i, document in enumerate(col, 1):
        file.write(json.dumps(document, default=str))
        if i != doc_count:
            file.write(',')
    file.write(']')

from dotenv import load_dotenv
import pymongo
import os
import json
import glob
import time


def exportToJson(db):
    start = time.time()
    col = db['jobs'].find({})
    doc_count = db['jobs'].count_documents({})
    print("Dumping documents to json...")
    with open("../../Data Storing/export/collection.json", "w") as file:
        file.write('[')
        # Start from one as type_documents_count also starts from 1.
        for i, document in enumerate(col, 1):
            file.write(json.dumps(document, default=str,
                       sort_keys=True, indent=4))
            if i != doc_count:
                file.write(',')
        file.write(']')
    print("Dump complete! " + str(time.time() - start))


def insertToMongo(db):
    start = time.time()
    col = db["jobs"]

    print("Removing old documents...")
    db.jobs.drop()
    print("Document(s) removed!")
    print("Inserting documents to database...")
    for f in glob.glob("../data/*_job.json"):
        file = open(f,)
        data = json.load(file)
        col.insert_one(data)
    print("Insert complete! " + str(time.time() - start))


def main():
    load_dotenv()
    server = os.getenv("SERVER_URL")
    starts = time.time()
    try:
        client = pymongo.MongoClient(
            host=server, serverSelectionTimeoutMS=2000)
        client.server_info()
    except:
        print("Connection error")
        print("Please check if server is running")
        print("Time elapsed: " + str(time.time() - starts))
        return

    db = client["basdat"]
    insertToMongo(db)
    exportToJson(db)

    client.close()
    print("Done! took " + str(time.time() - starts) + " second")


main()

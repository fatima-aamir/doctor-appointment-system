from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["devops"]  
doctors_collection = db["doctors"]

@app.route('/hello')
def hello():
    greeting = "Hello world!"
    return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():
    # Fetch doctors from MongoDB
    doctors = list(doctors_collection.find({}, {"_id": 0}))
    return jsonify(doctors)

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
    # Fetch a specific doctor from MongoDB by id
    doctor = doctors_collection.find_one({"id": id}, {"_id": 0})
    if doctor:
        return jsonify(doctor)
    else:
        return jsonify({"error": "Doctor not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["devops"]  
appointments_collection = db["appointments"]

@app.route('/hello')
def hello():
    greeting = "Hello world!"
    return greeting

@app.route('/appointments', methods=["GET"])
def getAppointments():
    # Fetch appointments from MongoDB
    appointments = list(appointments_collection.find({}, {"_id": 0}))
    return jsonify(appointments)

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
    # Fetch a specific appointment from MongoDB by id
    appointment = appointments_collection.find_one({"id": id}, {"_id": 0})
    if appointment:
        return jsonify(appointment)
    else:
        return jsonify({"error": "Appointment not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)

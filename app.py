from flask import Flask, jsonify
import requests

app = Flask(__name__)

HEADERS = {
    "authorization": "Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6IjI2YjM0NDgwLWQ5ZDEtNDQ4NS1iYzczLTRiN2IxOGJiOWUyNCIsInR5cCI6IkpXVCJ9.eyJhdWQiOltdLCJjbGllbnRfaWQiOiJjbGllbnRfYm1BbFFKZ0Q3eUw5RnFRVEkyT0dtUSIsImV4cCI6MTc5MTM1OTAxMiwiZXh0Ijp7Imdyb3VwX2lkIjoiNThhNGQ5MzEtMTZhZi00MGY5LWI0ZmYtOGExNDU4YzA2ZjNkIiwic2Vzc2lvbl9pZCI6ImZjNWJkZWZhLTUxZjgtNGU5NS04OGNmLTQ5MzZjY2UzY2M3ZCIsInVzZXJfdHlwZSI6IkVYVEVSTkFMIn0sImlhdCI6MTc5MTI3MjYxMSwiaXNzIjoiaHR0cHM6Ly9hdXRoLmNhcnMyNC5jb20vIiwianRpIjoiMDNmMjFkNDUtZmUyZS00MDMyLThiZTctN2VjMjBhMzRkZTUwIiwibmJmIjoxNzkxMjcyNjExLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiXSwic3ViIjoiM2U0ODk3ZTItODRmYi00Yjc1LWEwYzYtZDE0MDEzZDZhOGU3In0.8TEOsbbMvXgwKYLe8UgZPmRJTVqWexFLgIIegP1ORzajeiFW2chk1pqYWTt4T11K-wzSNBxiqnNkVg48o777dQ",
    "x-tenant-id": "VI_INDIA",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Mobile Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "origin": "https://vehicleinfo.app",
    "referer": "https://vehicleinfo.app/"
}

BASE_URL = "https://api-c24.vehicleinfo.app/gw/plt/bffsvc/api/v1/pages/challan"

# Map vehicle number → lead_token
VEHICLE_MAP = {
    "GJ27FJ3073": "66d253212546e9b8e3720371045190de63baa9448b"
}

@app.route("/challan/<vehicleno>", methods=["GET"])
def get_challan_by_vehicle(vehicleno):
    lead_token = VEHICLE_MAP.get(vehicleno.upper())
    if not lead_token:
        return jsonify({"error": "Vehicle number not mapped"}), 404

    url = f"{BASE_URL}/{lead_token}"
    resp = requests.get(url, headers=HEADERS)
    return jsonify(resp.json()), resp.status_code

if __name__ == "__main__":
    app.run()

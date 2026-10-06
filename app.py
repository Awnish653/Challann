from flask import Flask, jsonify
import requests

app = Flask(__name__)

HEADERS = {
    "authorization": "Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6IjI2YjM0NDgwLWQ5ZDEtNDQ4NS1iYzczLTRiN2IxOGJiOWUyNCIsInR5cCI6IkpXVCJ9....",  # full token from your capture
    "x-tenant-id": "VI_INDIA",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Mobile Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "origin": "https://vehicleinfo.app",
    "referer": "https://vehicleinfo.app/"
}

BASE_URL = "https://api-c24.vehicleinfo.app/gw/plt/bffsvc/api/v1/pages/challan"

@app.route("/challan/<vehicleno>", methods=["GET"])
def get_challan(vehicleno):
    # Step 1: fetch challan page for vehicle number
    first_url = f"{BASE_URL}?regNumber={vehicleno}"
    first_resp = requests.get(first_url, headers=HEADERS)
    if first_resp.status_code != 200:
        return jsonify({"error": "Vehicle lookup failed"}), first_resp.status_code

    data = first_resp.json()
    lead_token = data.get("clevertap", {}).get("challan_listing_viewed", {}).get("user_properties", {}).get("challan_lead_token")

    if not lead_token:
        return jsonify({"error": "Lead token not found"}), 404

    # Step 2: fetch challan details using lead_token
    second_url = f"{BASE_URL}/{lead_token}"
    second_resp = requests.get(second_url, headers=HEADERS)
    return jsonify(second_resp.json()), second_resp.status_code

if __name__ == "__main__":
    app.run()

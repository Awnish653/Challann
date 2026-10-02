from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://api-ct.carinfo.app/gw/plt/bffctsvc/api/v1/pages/challan/guest/search"

HEADERS = {
    "host": "api-ct.carinfo.app",
    "sec-ch-ua-platform": "\"Android\"",
    "source": "m-web",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Mobile Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "x-tenant-id": "CI_INDIA",
    "sec-ch-ua-mobile": "?1",
    "origin": "https://www.carinfo.app",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.carinfo.app/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
    "priority": "u=1, i"
}

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "Flask challan API running on Vercel"})

@app.route('/challan', methods=['GET'])
def challan_lookup():
    reg_number = request.args.get("regNumber")
    if not reg_number:
        return jsonify({"error": "regNumber parameter required"}), 400

    try:
        url = f"{BASE_URL}?regNumber={reg_number}"
        resp = requests.get(url, headers=HEADERS)

        if resp.status_code == 200:
            return jsonify(resp.json())  # full JSON response
        else:
            return jsonify({"error": f"Failed with status {resp.status_code}", "details": resp.text}), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

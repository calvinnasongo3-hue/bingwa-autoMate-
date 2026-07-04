from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Bingwa autoMate backend is running!"

@app.post("/mpesa/callback")
def callback():
    data = request.get_json(silent=True)
    print(data)
    return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

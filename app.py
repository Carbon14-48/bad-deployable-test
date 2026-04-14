from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "message": "This app has vulnerabilities!",
        "status": "running"
    }

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)

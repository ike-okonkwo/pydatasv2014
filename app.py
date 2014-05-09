from flask import Flask, request, render_template, jsonify
from yhat import Yhat
import pdb
app = Flask(__name__)

yh = Yhat("<USERNAME>", "<API KEY>", "http://cloud.yhathq.com/")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    article = request.form['article']
    results = yh.predict("documentClf", { 'content': article })
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run()
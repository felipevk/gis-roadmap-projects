from flask import Flask, render_template, jsonify
import db

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/data')
def data():
    # Only returns json, frontend will fetch via js
    return jsonify(db.getCombineAll())

if __name__ == '__main__':
    app.run(debug=True)
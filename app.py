from flask import Flask, jsonify, request

app = Flask(__name__)

# API to test connection
@app.route('/hello', methods=['GET'])
def test_connection():
    return jsonify({'message': 'Hello!'})




if __name__ == '__main__':
    app.run(debug=True)

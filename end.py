import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from sql import datas

t = datas()

app = Flask(__name__)
CORS(app)
# Create an empty array for passing data from backend to frontend
data_array = []

# Handling POST requests
@app.route('/api/data', methods=['POST'])
def receive_post_data():
    try:
        data = request.data.decode('utf-8')
        # Parse the JSON data
        data_dict = json.loads(data)
        
        # Format the data before storing it
        formatted_data = f"{data_dict['expression']}={data_dict['result']}"

        t.insert_data(formatted_data)
        data_array.append(formatted_data)

        return jsonify(message="Data received successfully"), 200
    except Exception as e:
        return jsonify(error=str(e)), 500



    

# Handles GET requests, passing the array to the front-end
@app.route('/api/data', methods=['GET'])
def send_get_data():
    data = t.read_data()
    data_array = data
    return jsonify(data_array)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
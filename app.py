from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Load data from CSV file
def load_data():
    data = {}
    with open('truck_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            location = row['LOCATION']
            data[location] = row
    return data

# Search for trucks based on location
@app.route('/search', methods=['GET'])
def search_trucks():
    location = request.args.get('location')
    truck_data = load_data()
    if location in truck_data:
        return jsonify(truck_data[location])
    else:
        return jsonify({'error': 'Location not found'})

if __name__ == '__main__':
    app.run(debug=True)

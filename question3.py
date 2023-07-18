# This is Question 3 of the assignment.
# We Would be choosing a configuration file that was created in json format that has
# several API keys, email id's, usernames etc.

'''
In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

●       The program should read a configuration file (you can provide them with a sample configuration file).

●       It should extract specific key-value pairs from the configuration file.

●       The program should store the extracted information in a data structure (e.g., dictionary or list).

●       It should handle errors gracefully in case the configuration file is not found or cannot be read.

●       Finally save the output file data as JSON data in the database.

●       Create a GET request to fetch this information.

'''
from flask import Flask, render_template, request, redirect, url_for
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def display_json():
    with open('data.json') as file:
        data = json.load(file)

    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    # Get form inputs
    api_name = request.form['api_name']
    api_username = request.form['api_username']
    api_key = request.form['api_key']

    # Create dictionary object
    new_data = {
        "api-name": api_name,
        "api-username": api_username,
        "api-key": api_key
    }

    # Read existing JSON data
    with open('data.json') as file:
        json_data = json.load(file)

    # Append new data to existing JSON data
    json_data.append(new_data)

    # Write the updated JSON data back to the file
    with open('data.json', 'w') as file:
        json.dump(json_data, file, indent=4)

    return '''
        <h2>Data submitted successfully!</h2>
        <p>Click the button below to go back to the main page:</p>
        <form action="/" method="get">
            <button type="submit">Go to Main Page</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(port=3000, debug=True)




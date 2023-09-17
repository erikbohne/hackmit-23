from flask import Flask, render_template
from flask import Flask, request, render_template, jsonify
import requests
from datetime import datetime, timedelta

import json




API_KEY = "ESqAayVypWYUfBreKU6bxtVrFpxoqnpk"
DEV_ID = "hackmit-testing-teLPulJ7ER"
SECRET = "b02af50cbd3127afcb1fc52d18269a2c005f3eccdcc9e56e" # ngrok webhook signing secret 


app = Flask(__name__)

@app.route('/')
def index():
    # Get the query parameters from the URL
    user_id = request.args.get('user_id')
    reference_id = request.args.get('reference_id')
    resource = request.args.get('resource')
    lan = request.args.get('lan')








    # Calculate the end date as today
    end_date = datetime.today() # Maybe change this to: .tomorrow()

    # Calculate the start date as one month ago from today
    start_date = end_date - timedelta(days=250) # should be 30

    # Convert the dates to the desired format ('YYYY-MM-DD')
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')






    url = f"https://api.tryterra.co/v2/activity?user_id={user_id}&start_date={start_date_str}&end_date={end_date_str}&to_webhook=false&with_samples=false"

    headers = {
        "accept": "application/json",
        "dev-id": "hackmit-testing-teLPulJ7ER",
        "x-api-key": "ESqAayVypWYUfBreKU6bxtVrFpxoqnpk"
    }

    response = requests.get(url, headers=headers)



    #print('\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n')

    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', data=data)
    else:
        return "Error fetching data from the API. Try reauthenticating.", 500
  

import json
def filter_data(data):
    if isinstance(data, dict):
        filtered_data = {}
        for key, value in data.items():
            if value is not None:
                if isinstance(value, (int, float)) and value == 0:
                    continue
                elif isinstance(value, (str, list)) and not value:
                    continue
                elif isinstance(value, dict):
                    if key not in ["polyline_map_data", "position_data"] and bool(value):
                        filtered_value = filter_data(value)
                        if filtered_value:
                            filtered_data[key] = filtered_value
                else:
                    filtered_data[key] = filter_data(value)
        return filtered_data
    elif isinstance(data, list):
        filtered_data = []
        for item in data:
            filtered_item = filter_data(item)
            if filtered_item:
                filtered_data.append(filtered_item)
        return filtered_data
    else:
        return data


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # Parse the JSON data from the POST request
   
    filtered_data = filter_data(data)
    

     # Now you can access data['data']
    if 'data' in filtered_data:

        # Save the filtered data to a JSON file
        with open('filtered_data.json', 'w') as file:
            json.dump(filtered_data, file, indent=2)
        
    

            print('EXCERCISE SESSION RECIEVED TO WEBHOOK')
            return jsonify({'message': 'Webhook received', 'data': filtered_data}), 202 # This 202 response can be used as a trigger client-side in javascript. Ask ChatGPT further.


        

    #print('REGULAR WEBHOOK RECIEVED')
    return jsonify({'message': 'Regular Webhook received'})
    


@app.route('/fail')
def fail():
    return render_template('fail.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051, debug=True)

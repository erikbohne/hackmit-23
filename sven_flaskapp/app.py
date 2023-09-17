from flask import Flask, render_template
from flask import Flask, request, render_template
import requests
from datetime import datetime, timedelta

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



    # MILKSHAKE RUN 
    start_date_unix_seconds = '2023-09-13' # These arguments also takes unix-seconds
    end_date_unix_seconds = '2023-09-17'



    url = f"https://api.tryterra.co/v2/activity?user_id={user_id}&start_date={start_date_unix_seconds}&end_date={end_date_unix_seconds}&to_webhook=false&with_samples=false"

    headers = {
        "accept": "application/json",
        "dev-id": "hackmit-testing-teLPulJ7ER",
        "x-api-key": "ESqAayVypWYUfBreKU6bxtVrFpxoqnpk"
    }

    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', data=data)
    else:
        return "Error fetching data from the API", 500


@app.route('/fail')
def fail():
    return render_template('fail.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051, debug=True)

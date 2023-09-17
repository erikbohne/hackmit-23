from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint



# Strava api variables:
CLIENT_ID = 113778
CLIENT_SECRET = '2d553934e797beefdaf7e0b4ad5b043323383598'

REFRESH_TOKEN = 'b3f5d1ae070c85a2b0d34064edf58755875329cf' # Recieved from authentication
ACCESS_TOKEN = '36961145d6c86acc58c86847f0b8368e2db3bcad'  # Recieved from authentication


AUTHORIZATION_CODE = '99ca4a5b87bc10b9861c8048f04a68780cc43956' # From url after redirect from authentication



auth_url = f"http://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read"


auth_url = f"http://www.strava.com/oauth/authorize?client_id=113778&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read"

auth_url = f"http://www.strava.com/oauth/authorize?client_id=113778&response_type=code&redirect_uri=https://developers.strava.com/exchange_token&approval_prompt=force&scope=read"





# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = ACCESS_TOKEN

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 789 # Long | The identifier of the activity.
includeAllEfforts = True # Boolean | To include all segments efforts. (optional)

try: 
    # Get Activity
    api_response = api_instance.getActivityById(id, includeAllEfforts=includeAllEfforts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)


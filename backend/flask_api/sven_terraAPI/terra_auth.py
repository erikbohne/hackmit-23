from terra.base_client import Terra

# Static:
API_KEY = "ESqAayVypWYUfBreKU6bxtVrFpxoqnpk"
DEV_ID = "hackmit-testing-teLPulJ7ER"
SECRET = "b02af50cbd3127afcb1fc52d18269a2c005f3eccdcc9e56e" # ngrok webhook signing secret 

# Change to fit enviroment:
REDIRECT_URL = "https://23f4-192-54-222-143.ngrok-free.app" # This should correspond to the url of where the web-app is hosted. It needs to be exposed to the internet.
my_reference_id = "username@test.com" # In-app username which can be used as an alias for user_id. 



terra = Terra(API_KEY, DEV_ID, SECRET)

auth_resp = terra.generate_authentication_url(
  reference_id=my_reference_id,
	resource="STRAVA",
	auth_success_redirect_url = REDIRECT_URL + "/?user_id=wow_a_new_user&reference_id=fun_identifier&resource=STRAVA",
  auth_failure_redirect_url = REDIRECT_URL + "/fail",
).get_parsed_response()

#print(auth_resp)



# This link should be displayed on the web-app in some way. 
# The user clicks it and thereby verifies/autheticates the user_id below such that it can be used for api-requests later.
print('\n-------- REFERENCE ID:  -----------')
print(my_reference_id)

print('\n-------- USER ID:  ----------------')
print(auth_resp.user_id)

print('\n-------- AUTHENTICATION URL:  -----') 
print(auth_resp.auth_url)

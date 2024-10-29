import requests
from neo_api_client import NeoAPI
import base64
from dotenv import load_dotenv
import os
load_dotenv()  # Load .env file

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
consumer_key_plus_secret = consumer_key+":"+consumer_key
consumer_key_plus_secret_bytes = consumer_key_plus_secret.encode("ascii")
consumer_key_plus_secret_base64_bytes = base64.b64encode(
    consumer_key_plus_secret_bytes)
consumer_key_plus_secret_base64_bytes_cleaned_string = str(
    consumer_key_plus_secret_base64_bytes)[2:-1]
Authorization = consumer_key_plus_secret_base64_bytes_cleaned_string
api_username = os.getenv("API_USERNAME")
api_password = os.getenv("API_PASSWORD")
Neo_fin_key = os.getenv("NEO_FIN_KEY")
# user_id =
mobile_number = os.getenv("MOBILE_NUMBER")
neo_login_mpin = os.getenv("NEO_LOGIN_MPIN")


# Generate Auth token
headers = {
    'Authorization': 'Basic ' + Authorization,
}
print(headers)
data = {
    'grant_type': 'password',
    'username': api_username,
    'password': api_password,
}
AuTh = requests.post('https://napi.kotaksecurities.com/oauth2/token',
                     headers=headers, data=data, verify=True)
print(AuTh.json())

# Login
access_token = os.getenv("ACCESS_TOKEN")
headers = {
    'Authorization': 'Bearer '+access_token,
}
json_data = {
    "mobileNumber": mobile_number,
    "mpin": neo_login_mpin,
}
login2 = requests.post(
    "https://gw-napi.kotaksecurities.com/login/1.0/login/v2/validate", headers=headers, json=json_data)
print(login2.json())

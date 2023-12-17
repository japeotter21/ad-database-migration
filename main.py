import requests
from requests.auth import HTTPBasicAuth
from dotenv import dotenv_values
config = dotenv_values(".env")
authToken = HTTPBasicAuth(config['CB_USER'],config['CB_PASS'])
baseUrl = 'http://35.196.111.98:8093/query/service?statement='
queryString = 'SELECT * FROM `release-service` WHERE `key` = "audit" AND `user` = 0'
fullUrl = baseUrl+queryString
r = requests.post(fullUrl, auth=authToken)
resultObj = r.json()['results']
releaseService = resultObj[0]['release-service']['data']

for audit in releaseService:
    print(audit)
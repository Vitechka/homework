import http.client
import json

connection = http.client.HTTPSConnection("belarusbank.by")
headers = {'Content-type': 'application/json'}
connection.request("GET", "/api/kursExchange")
response = connection.getresponse()
response_body = response.read().decode('utf-8')
#print("Status: {} and reason: {}".format(response.status, response.reason))
#print(response.read())
response_json = json.loads(response_body)
print(response_json[0]["USD_in"])
print(response_json[0]["USD_out"])

print(response_json[0]["name"])
connection.close()


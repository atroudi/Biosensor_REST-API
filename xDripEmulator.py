#emulate a POST request from xDrip Application
import requests

reading = {u'direction': u'Flat', u'noise': 1, u'sysTime': u'2018-05-24T17:11:17.138+0300', u'dateString': u'2018-05-24T17:11:17.138+0300', u'sgv': 73, u'date': 1527171077138, u'unfiltered': 3294, u'delta': 0, u'device': u'xDrip-LimiTTer', u'filtered': 3294, u'type': u'sgv', u'rssi': 100}
headers = {'api-secret': 'asdasd'}

# Read entries file
import ast

with open('entries.txt', 'r') as f:
    entries = ast.literal_eval(f.read())
# print(entries[0].get('direction'))
print(entries[0])
for entry in entries[100:101]:
    res = requests.post('http://192.168.43.247:5000/api/v1/entries', json=entry)
    # res = requests.post('http://localhost:8000/api/records/', json=entry, headers=headers, auth=('anistroudi@gmail.com', 'qatar123'))
    # res = requests.post('http://atroudi@gmail.com:qatar123@localhost:8000/api/records/', json=entry, headers=headers)
    # res = requests.post('http://patient1@gmail.com:qatar123@104.45.17.144:80/api/records/', json=entry, headers=headers)

# res = requests.post('http://asdasd@localhost:1337/api/v1/verifyauth', json=reading)

print ('response from server:',res.text)

# dictFromServer = res.json()


print("Stored %d entry" % (len(entries)))

print(entries[0])

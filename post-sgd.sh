#!/bin/sh
# Date is epoch in nanosecods...ie linux echo $(($(date +%s%N)/1000000))
# $API_SECRET needs to be a hashed value of your secret key...ie linux echo -n "<API_SECRET>" | sha1sum


s="{u'direction': u'Flat', u'noise': 1, u'sysTime': u'2018-05-24T17:11:17.138+0300', u'dateString': u'2018-05-24T17:11:17.138+0300', u'sgv': 73, u'date': 1527171077138, u'unfiltered': 3294, u'delta': 0, u'device': u'xDrip-LimiTTer', u'filtered': 3294, u'type': u'sgv', u'rssi': 100}"
s.rep
# Curling Biosensors REST_API
curl -H "Content-Type: application/json" -H "api-secret: asdasd" -XPOST 'http://localhost:5000/api/v1/entries' -d "{u'direction': u'Flat', u'noise': 1, u'sysTime': u'2018-05-24T17:11:17.138+0300', u'dateString': u'2018-05-24T17:11:17.138+0300', u'sgv': 73, u'date': 1527171077138, u'unfiltered': 3294, u'delta': 0, u'device': u'xDrip-LimiTTer', u'filtered': 3294, u'type': u'sgv', u'rssi': 100}"

# Curling Biosensors REST_API Backup
# curl -H "Content-Type: application/json" -H "api-secret: asdasd" -XPOST 'http://localhost:5000/api/v1/entries' -d '{
#   "sgv": 100,
#   "type": "sgv",
#   "direction": "Flat",
#   "date": 1449872210706
# }'

# Curling nightscout
# curl -H "Content-Type: application/json" -H "api-secret: 9ecee12ad8d58775d3f966131955ffdab7dfc6d2" -XPOST 'http://localhost:1337/api/v1/entries/' -d '{
#   "sgv": 100,
#   "type": "sgv",
#   "direction": "Flat",
#   "date": 1449872210706
# }'


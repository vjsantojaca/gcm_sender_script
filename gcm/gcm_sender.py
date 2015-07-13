import requests
import MySQLdb
import json

url = 'https://android.googleapis.com/gcm/send'
data = { 'message' : message }
reg_ids = []
payload = {}


db = MySQLdb.connect(host="", # mysql host
				user="", # your username bd
				passwd="", # your password bd
				db="") # name of the data base

cur = db.cursor() 

cur.execute("") #Select to obtain the ids (get ids to database)

num_user = 0

for row in cur.fetchall() :
	reg_ids.insert(num_user, row[0])
	num_user = num_user + 1

db.close()

payload['registration_ids'] = reg_ids
payload['data'] = data
payload['collapse_key'] = '' #the app key
payload = json.dumps(payload)

dat2 = dict(registration_ids = reg_ids, data = dict(message=message))

try:
	headers = {
		'Authorization':'key=XXXXXX', #the app key
		'Content-Type':'application/json'
	}

	response = requests.post(url=url, data=payload, headers=headers, proxies=None)

	print response.content
	print response.status_code
except Exception as ex: print ex
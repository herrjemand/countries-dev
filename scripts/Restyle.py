#!/usr/bin/python3

# Author: Ackermann Yuriy < herrniemand@github > < ackermann.yuriy@gmail.com >

# This is ugly code
# Author had not time to make it pretty, pretty princes
# So if you are not happy with it, please fix it.

import json
x = {}
File = {
	'origin': 'countries.json',
	'saveto': 'countries.temp.json'
}
with open(File['origin']) as f:
	x = json.loads(f.read())
 
 
jzon = ''
for i in x:
	codes = {}
	order = [
		"name",
		"tld",
		"cca2",
		"ccn3",
		"cca3",
		"currency",
		"callingCodes",
		"capital",
		"altSpellings",
		"region",
		"subregion",
		"languages",
		"translations",
		"latlng",
		"demonym",
		"landlocked",
		"borders",
		"area"
	]
	for item in order:
		codes[item] = '"' + item + '":'

	for n in i:
		if type(i[n]) in [str,int,float,list,bool]:
			codes[n] = codes[n] + ' ' + json.dumps(i[n])
		else:
			if n in ['languages']:
				codes[n] = codes[n] + " {\n"
				if len(i['languages'].keys()):
					for z in sorted(i[n]):
						codes[n] = codes[n] + "\t\t\t\"" + z + "\": " + json.dumps(i[n][z]) + ",\n"
					codes[n] = codes[n][:-2] + '\n'
					codes[n] = codes[n] + "\t\t}"
				else:
					codes[n] = codes[n][:-1:] + '}'
		
			elif n == 'translations':
				codes[n] = codes[n] + ' {\n'
 
				if len(i['translations'].keys()):
					for k in sorted(i['translations'].keys()):
						codes[n] += '\t'*3 + '"' + k + '": { ' \
						+ '\"official\": ' + json.dumps(i['translations'][k]['official']) + ','\
						+ ' ' + '\"common\": ' + json.dumps(i['translations'][k]['common'])\
						+ ' },\n'
 
					codes[n] = codes[n][:-2:]
					codes[n] += '\n\t\t}'
				else:
					codes[n] = codes[n][:-1:] + '}'
 
			elif n == 'name':
				codes[n] = codes[n] + ' {\n' \
				+ '\t'*3 + '\"common\": ' + json.dumps(i[n]['common']) + ',\n' \
				+ '\t'*3 + '\"official\": ' + json.dumps(i[n]['official']) + ',\n' \
				+ '\t'*3 + '\"native\": {\n'
				if len(i['name']['native'].keys()):
					for k in sorted(i['name']['native'].keys()):
						codes[n] += '\t'*4 + '"' + k + '": {\n' \
						+ '\t'*5 + '\"official\": ' + json.dumps(i['name']['native'][k]['official']) + ',\n'\
						+ '\t'*5 + '\"common\": ' + json.dumps(i['name']['native'][k]['common'])  + '\n'\
						+ '\t'*4 + '},\n'
 
					codes[n] = codes[n][:-2:]
					codes[n] += '\n' + '\t'*3 + '}\n\t\t}'
				else:
					codes[n] = codes[n][:-1:] + '}\n\t\t}'
 
 
	string = ''
	for i in order:
		
			string = string + '\t\t' + codes[i] + ",\n"
	jzon += '\n\t{\n' + string[:-2] + '\n\t},'
 
jzon = '[\n' + jzon[:-1] + '\n]'
 
with open(File['saveto'],'w') as w:
	w.write(jzon)

habababa = ''
print('Validating json...')
with open(File['saveto']) as f:
	try:
		habababa = json.loads(f.read())
		print('V : Validating passed : V')

	except Exception as e:
		print('X : Validating failed : X')
		print(e)
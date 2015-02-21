# Author: Ackermann Yuriy < herrniemand@github > < ackermann.yuriy@gmail.com >

from lxml import html #pip install lxml ...p.s. might have to build it from the source.
import requests, time, os.path, json

save_to = 'flags_new' #folder where you want to save. NO /(Forward slash) !

temp_data, data = {}, {}
errors = 'Errors: \n'

def stripper(c_name):
	print('Doing: ', c_name)

	page = requests.get('https://en.wikipedia.org/wiki/File:Flag_of_' + c_name + '.svg') #loads the webpage
	tree = html.fromstring(page.text) #html to xpath tree
	link = ''.join(tree.xpath('//*[@id="file"]/a/img/../@href')) #getting svg links
	
	return link

def save(link,cca3):
	with open(save_to + '/' + cca3.lower() + '.svg','w') as w:
			w.write(requests.get('https:' + link).text) #saving image
			print("Done\n")
			time.sleep(1) #one second delay, to ensure that host will not think that we dos attack him


with open('countries.json') as r: #loads the countries data
	temp_data = json.loads(r.read())

for i in temp_data: #restructure it from the list to dictionary
	data[i['name']['common']] = i

for key in data.keys():
	link = ''
	for i in ['common','official']: 
		link = stripper(data[key]['name'][i])
		if link:
			print(link)
			save(link,data[key]['cca3'])
			break
	
	else:
		errors += data[key]['cca3'].lower() + ' ' + data[key]['name']['common'] + '\n' #Saves list of errors in loading flags
		print("Error Retrieving Flag: ", '\s\s\s', data[key]['cca3'].lower(), '\s\s\s', data[key]['name']['common'],'\n')

print('\n\n',errors) #print errors

with open('errors_flags.txt','w') as w:
	w.write(errors) #writes errors to file
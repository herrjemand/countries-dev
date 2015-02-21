# Author: Ackermann Yuriy < herrniemand@github > < ackermann.yuriy@gmail.com >

#Need to do `pip install Translate`
import json
from translate import Translator

trid = {
	'alpha2' : 'fi', #Example with Finnish language
	'alpha3' : 'fin'
}

lang, temp_data, data = {}, [], []
with open('countries.json') as r:
	temp_data = json.loads(r.read())

for i in temp_data:
	translator= Translator(to_lang = trid['alpha2'])

	i['translations'][trid['alpha3']] = {}
	i['translations'][trid['alpha3']]['official'] = translator.translate(i['name']['official'])
	i['translations'][trid['alpha3']]['common'] = translator.translate(i['name']['common'])

	data.append(i)

	print("Done ", i['name']['common'])

with open('countries.temp.json','w') as w:
	w.write(json.dumps(data, indent=4, separators=(',', ': ')))

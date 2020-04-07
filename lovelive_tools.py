import requests
says=[]
for i in range(200):
	html = requests.get('https://api.lovelive.tools/api/SweetNothings/:count')
	says.append(html.text)
	print(i)
	with open('lovelive.txt','a') as f:
		f.write(html.text+'\n')


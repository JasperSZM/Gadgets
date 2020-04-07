import requests
says=[]
num_of_says = 200
for i in range(num_of_says):
	html = requests.get('https://api.lovelive.tools/api/SweetNothings/:count')
	says.append(html.text)
	print(i)
	with open('lovelive.txt','a') as f:
		f.write(html.text+'\n')


import requests
import re
import time
import img2pdf
import os

def gethtml(url):
  j = 0
  while j < 4:
    try:
        print('Try to download')
        html = requests.get(url, timeout=10)
        return html
    except requests.exceptions.RequestException:
        j += 1

print("For downloading comic on vlcomic.com")
time.sleep(1)
print("Please input the address of website.")
weburl=input()
html = gethtml(weburl)
listimg = re.findall(r'img src="(.*?)"',html.text)
print('\n')
print('Get the page! Ready to download...')
time.sleep(1)
print('There are '+str(len(listimg))+' pages and it will take a long time.')
print('\n')
i=0
for url in listimg:
	i = i+1
	print('Downloading '+str(i))
	htmlimg = gethtml(url)
	#htmlimg = requests.get(url)
	with open(str(i)+".jpg","wb")as f:
		f.write(htmlimg.content)
	print(str(i)+' finished')
	print('\n')
	time.sleep(1)
	
listjpg=[]
for j in range(i):
	listjpg.append(str(j+1)+'.jpg')
#print(listjpg)
print('Please input the name of pdf:')
name = input()
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4inpt)
with open(str(name)+'.pdf','wb') as f:
    f.write(img2pdf.convert(listjpg,layout_fun=layout_fun))

for j in range(i):
	os.remove(str(j+1)+'.jpg')

print('Finish! Welcome to UtoSpace to explore more! www.utospace.club')
time.sleep(5)

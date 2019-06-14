import webbrowser
import pyqrcode
from googlesearch import search
import os
data=input('Enter your search--->>')
webbrowser.open_new_tab('https://www.google.com/search?q='+data)
list=[]
for i in search(data,stop=3):
	list.append(i)
j=1
for i in list:
	c=pyqrcode.create(i)
	c.svg(str(j)+'.svg',scale=8)
	j=j+1

file=input('Enter name of .html file :')

os.system('touch'+' '+file)
os.system('echo "<html><h1>QR code for your search :</h1><body><img src="1.svg"><img src="2.svg"><img src="3.svg"></body></html>">'+file )
os.system('sudo mv '+file+' '+'/var/www/html/' )
os.system('sudo mv 1.svg /var/www/html/' )
os.system('sudo mv 2.svg /var/www/html/' )
os.system('sudo mv 3.svg /var/www/html/' )



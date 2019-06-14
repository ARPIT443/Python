import webbrowser
import pyqrcode
from googlesearch import search
data=input('Enter your search--->>')
webbrowser.open_new_tab('https://www.google.com/search?q='+data)
list=[]
for i in search(data,stop=3):
	list.append(i)
j=1
for i in list:
	c=pyqrcode.create(i)
	c.svg("qrcode"+str(j),scale=8)
	j=j+1



from googlesearch import search
import webbrowser

url=input('Enter your search')
list=[]
for i in search(url,stop=10):
	list.append(i)

f=open('url_list.txt','w')
for i in list:
	f.write(i)
	f.write('\n')
f.close()

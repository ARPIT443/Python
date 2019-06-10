
from googlesearch import search
import webbrowser
import time
url=input('Enter your search : ')
list=[]
for i in search(url,stop=5):
        list.append(i)
for i in list:
        webbrowser.open_new_tab(i)
        time.sleep(2)

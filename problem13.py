import pyttsx3
import datetime
sound_driver=pyttsx3.init()
sound_driver.say("Hello,Arpit")
sound_driver.runAndWait()

s=datetime.datetime.now().hour

if s in range(0,12):
	sound_driver.say("Good Morning")
elif s in range(12,18):
	sound_driver.say("Good afternoon")
elif s in range(18,22):
	sound_driver.say("Good Evening")
else:
	sound_driver.say("Good night")

sound_driver.runAndWait()

def add(*x):
	sum=0
	for i in x:
		sum=sum+i
	print('Sum is : '+str(sum) )

def sort(*x):
	print(sorted(x))

def module_info():
	help('modules')




	
		

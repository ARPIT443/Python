import datetime
now = datetime.datetime.now().hour
name=input('Enter your name')
if now  in range(0,12):
	print('Hello'+name+',Good Morning..!')

elif now  in range(12,18):
	print('Hello'+name+',Good Afternoon..!')

elif now  in range(18,22):
	print('Hello'+name+',Good Evening..!')

else:
	print('Hello'+name+',Good Night..!')

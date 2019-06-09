import datetime
name=input('Enter name of person :')
age=input('Enter current age :')
x=95-int(age)
current_year=datetime.datetime.now().year
y=current_year+x
print(name+' will turn to 95 in '+str(y))

########################################

import datetime

name=input('Enter name of person :')
age=input('Enter current age :')

x=95-int(age)
current_year=datetime.datetime.now().year #Show current year
year_at_95=current_year+x
print(name+' will turn to 95 in '+str(year_at_95))

#########################################

option='''
1. Create single file
2. Create multiple file 
3. touch -c Command
'''
print(option)

choice=input('Enter your choice :')

if choice=='1':
	fname=input('Enter name of file :')
	f=open(fname,'w')
	f.close()
	print('File created successfully')

elif choice=='2':
	num=int(input('Number of file you want to create :'))
	list=[]
	print('Enter files name seperated by enter :')
	for i in range(num):
		fnames=input()
		list.append(fnames)
	for i in list:
		f=open(i,'w')
		f.close()	
	print('Files created successfully')

elif choice=='3':
	fname=input('Enter name of file :')
	print('Command run successfully')
	exit()	
	

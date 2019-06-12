option = '''
	Select operation you want to perform--->>
	1.Show contents of single file :
	2.Show contents of multiple file :
	3.cat -n command :
	4.cat -E command :
'''

print(option)

choice=input()

if choice == '1':
	fname=input('Name of file :')
	f=open(fname,'r')
	print(f.read())
	f.close()
elif choice == '2':
	num=int(input('Enter no. of files :'))
	fnames=[]
	print('Enter name of files seperated by enter :')
	for i in range(1,num+1):
		name=input() 
		fnames.append(name)
	
	for i in fnames:
		f=open(i,'r')
		print(f.read())
		f.close()
elif choice == '3':
	fname=input('Name of file :')
	fopen
else:
	print('lol..!!')		
	
		
	
	
	
 

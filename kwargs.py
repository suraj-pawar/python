def VriableArgsDistionary(a,b,c,*args,**kwargs):
	print a,b,c
	print type(args)
	for x in args:
		print (x)

	print type(kwargs)
#	for key in kwargs:
#		print (key,kwargs[key])

	for key,value in kwargs.items():
		print (key,kwargs[key])



def main():
	VriableArgsDistionary(1,2,3,10,20,name="suraj",sname="pawar")

if __name__ == "__main__":
	main()	

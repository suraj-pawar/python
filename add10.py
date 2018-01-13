#!usr/bin/python/python2.7

#write a program to accept n no from user and add them

def my_generator():
	count=input("HOW MANY ")
	for x in range(count):
		i=input()			
		yield i		

def add(*args):
	tot=0
	for x in args:
		tot=tot+x	
	print tot


if __name__ == "__main__":
	it=my_generator()
	add(*it)





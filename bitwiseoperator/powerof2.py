#!usr/bin/python/python2.7

def powerof2(no):
	return (no & no-1) ==0
	

def main():
	input_no=input("Enter the no")
	result=powerof2(input_no)
	if result:
		print "no is 2's power"
	else:
		print "no is not 2's power"	

if __name__== "__main__":
	main()

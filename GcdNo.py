#!usr/bin/python/python2.7

def GCDfind(no1,no2):
	while no1!=no2:
		if no1>no2:
			no1=no1-no2
		else:
			no2=no2-no1
	return no1
	

def main():
	input_no1=input("Enter the 1st no")
	input_no2=input("Enter2the 2nd no")

	print "GCD of rwo no. is %d"%GCDfind(input_no1,input_no1)

if __name__ == "__main__":
	main()


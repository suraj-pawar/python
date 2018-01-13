#!usr/bin/python/python2.7

def GCDfind(no1,no2):
		if no1==no2:
			return no1
		if no1>no2:
			no1= no1-no2
		else:
			no2=no2-no1
		return GCDfind(no1,no2)


def main():
	input_no1=input("Enter the 1st no")
	input_no2=input("Enter2the 2nd no")
	result=GCDfind(input_no1,input_no1)

	print result
if __name__ == "__main__":
	main()



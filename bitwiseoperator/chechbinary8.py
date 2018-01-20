#!usr/bin/python/python2.7

def multipleof8(no):
#	if no<8:
#		return 0
#	else:
#		if no&7==0:
#			return no			
	return no & 7== 0
	
def main():
	input_no=input("Enter the no")
	result= multipleof8(input_no)
	if result:
		print "multiple of 8"
	else:
		print "no is not multiple of 8"

if __name__ == "__main__":
	main()



# in python promt 
# >>>bin(8)
#	1000

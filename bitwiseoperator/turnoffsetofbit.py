#!usr/python/python2.7

def turnoffsetofbits(no,noofbits,pos):
	x=1
	x=(2**noofbits)-1
	if noofbits<=pos:
		x=x<<(pos-noofbits)
		x=~x
		return no&x
	return -1
			
	

def main():
	no=input("ENter the no")
	noofbits=input("ENter the no of bits")
	pos=input("Enter the pos")
	
	print turnoffsetofbits(no,noofbits,pos)	

if __name__ == "__main__":
	main()

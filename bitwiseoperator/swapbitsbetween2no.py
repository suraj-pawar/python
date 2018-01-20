#!usr/bin/python/python2.7


def swapbits(no1,no2,pos,bits):
	x=no1
	y=no2
	
	mask=((2**bits)-1)<<(pos-bits)   # pos=5,bits=4 ---> 0001 1110
	
	xtemp= x & mask
	ytemp= y & mask

	x=x & (~ mask)
	y=y & (~ mask)

	x=x | ytemp
	y=y | xtemp 

 	return x,y
	
		
def main():
	no1=input("Enter the no1")
	no2=input("Enter the no2")
	pos=input("Enter the pos")
	bits=input("Enter the no of bits")
	print swapbits(no1,no2,pos,bits)

if __name__ == "__main__":
	main()

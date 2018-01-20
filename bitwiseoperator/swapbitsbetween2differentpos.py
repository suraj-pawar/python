#!usr/bin/python/python2.7

def swapbitsbetween2differentpos(no1,no2,pos1,pos2,bits):
	x=no1
	y=no2
	
	if pos1 > bits and pos2 >bits :
 
		mask1=((2**bits)-1) << (pos1-bits)
		mask2=((2**bits)-1) << (pos2-bits)

		xtemp=(x & mask1)
		ytemp=(y & mask2)

		x=x & (~mask1)
		y=y & (~mask2)

		if pos1>pos2:
			diff=pos1-pos2
			x=x | (ytemp<<diff)
			y=y | (xtemp>>diff)
		elif pos2>pos1:
			diff=pos2-pos1
			x=x | (ytemp>>diff)
			y=y | (xtemp<<diff)
		else:
			x=x | ytemp
			y=y | xtemp
		
		return x,y
	return -1


def main():
	no1=input("Enter no1")
	no2=input("Enter no2")
	pos1=input("Enter pos1 for no1")
	pos2=input("Enter pos2 for no2")
	bits=input("Enter no of bits")
	print swapbitsbetween2differentpos(no1,no2,pos1,pos2,bits)

if __name__ == "__main__":
	main()

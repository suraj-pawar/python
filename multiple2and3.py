#!usr/bin/python/python2.7


def multiple(l,u):
	for x in range(l,u+1):
		if x%2==0 and x%3==0:
			print x

def main():
	lower=input("Enter the lower bound")
	upper=input("Enter the upper bound")

	multiple(lower,upper)

if __name__ == "__main__":
	main()


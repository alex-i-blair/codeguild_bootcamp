import random

def get_number():
	t = raw_input("Guess a # between 1 and 100: ")
	t = int(t)
	return t

x = random.randint(1, 100)

while t != x:
	if t < x:  
		print "Too low"
	if t > x:
		print "Too high"
	t = get_number()
	
if t == x: 
	print "You got it!" 







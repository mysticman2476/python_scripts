# Simple program

username = raw_input ('Please enter your name: ')
age=input('Please enter your age: ')
print 'your name is {} and your age is {}'.format(username, age)

if age > 13:
	print ('You are officially a teen')
else:
	print ('you are a kid')

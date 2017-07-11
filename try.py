# Simple program

username = raw_input ('Please enter your name: ')
age=input('Please enter your age: ')

print 'your name is {} and your age is {}'.format(username, age)

if age > 18:
	print (username, 'you are officially a teen')
elif age == 15:
	print (username, 'you are 15!')
else:
	print (username, 'you are a kid')


print ('goodbye')

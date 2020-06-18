#Prints	the Words   “Hello World”
#print('"Hello World!!"')
print ("Everything is Great!!")

# This is a comment
# This is also a comment
# This is yet another comment

'''
The World is so Beautiful
This is a comment
Thank you PYTHON
'''
print  ('Successful')

#April 23 2020
#FORMATTING THE STRING

#brand	= ' Apple ’

#exchangeRate	=   1.235235245
	
#message	=   ‘The price of this %s laptop is %d	USD and the exchange rate is %4.2f  USD	to  1 EUR’  %(brand, 1299,  exchangeRate)
	
#print	(message)
'''
Error : EOL error. When copied and pasted and tried to execute it showed such error.
Also the variable message's assigned value was not shown in green which also indicates some error.
Similarly there should have been space between ' and Apple ' in the brand variable.
'''
brand = ' Apple '
exchangeRate = 1.234567890
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print (message)

#Second Method of formatting using format() instead of %
'''
Had the same error : EOL string literal identifier.
I found out that ' symbol when copy pasted was different for the editor.
So, i deleted and typed the symbol again to resolve the error.
'''

message	= 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)

#Third Method : We use format() method but without doing formatting operation

message	= 'The price of	this {}	laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format('Apple',
1299,	1.235235245)

#Examples of all types of formatting the string are given below

message1 ='{0} is easier than {1}'.format('Python', 'Java')
message2 ='{1} is easier than {0}'.format('Python', 'Java')
message3 ='{:10.2f} and	{:d}'.format(1.234234234, 12)
message4 ='{}'.format(1.234234234)
	
print (message1)
#You’ll	get	‘Python	is	easier	than	Java’
	
print (message2)
#You’ll	get	‘Java	is	easier	than	Python’
	
print (message3)
#You’ll	get	‘     1.23 and	12’
#You do	not need to indicate the positions of the parameters.
	
print (message4)
#You’ll	get 1.234234234. No formatting	is done.

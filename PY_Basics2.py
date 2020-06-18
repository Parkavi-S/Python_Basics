#LIST, TUPLE, DICTIONARY

#SYNTAX FOR LIST: listName  =	[initial values]
userAge	= [21,22,23,24,25]
'''
listName = [].	What we	have now is an	empty list with no items in it.
We have	to use the append() method mentioned below to add items	to the list.
'''

#declaring the list,list elements can be of different data types
myList	=   [1,	2,  3,	4,  5,	"Hello"]

#print	the	entire	list.
print(myList)	
#You’ll	get [1,	2, 3, 4, 5, “Hello”]

#print	the	third	item	(recall:	Index	starts	from zero).
print(myList[2])
#You’ll	get	3

#print	the	last	item.
print(myList[-1])
#You’ll	get	“Hello”
	
#assign	myList	(from	index	1 to 4)	to  myList2 and print myList2
myList2	=	myList[1:5]
print	(myList2)
#You’ll	get	[2,	3,	4,	5]
	
#modify	the second  item in  myList and print the updated list
myList[1] =	20
print(myList)
#You’ll	get[1,20,3,4,5,	'Hello']

#append	a new item  to	myList	and print the updated list
myList.append("How are you")
print(myList)
#You’ll	get [1,20,3,4,5,'Hello','How are you']

#remove	the sixth item	from myList and	print the updated list
del myList[5]
print(myList)
#You’ll	get [1,	20, 3,	4,  5,	'How are you']


#TUPLES
#tupleName  =	(initial values)

monthsOfYear =	("Jan", "Feb","Mar","Apr","May", "Jun", "Jul", "Aug","Sep","Oct","Nov","Dec")
#print(monthsOfYear) if given is asking for the command line argument sys.argv(). Need to check.

print (monthsOfYear[0])

# The above print statement asked for command line argument sys.argv: When given Value 1, the output was jan.

print (monthsOfYear[-1])


#DICTIONARY
'''
dictionaryName	=   {dictionary key	:   data},
with the requirement that dictionary keys must	be  unique (within one dictionary).

'''

#Method1 declaration
userNameAndAge	= {"Peter":38,"John":51,"Alex":13, "Alvin":"Not Available"}
print(userNameAndAge)

#Method2 declaration
userNameAndAge1	= dict(Peter =	38, John = 51,	Alex = 13, Alvin = "Not Available")
print(userNameAndAge1)

#declaring the	dictionary, dictionary	keys and data can be of	different data	types
myDict	=   {"One":1.35, 2.5:"Two Point Five",	3:"+", 7.9:2}

#print	the entire  dictionary

print(myDict)
#You’ll	get	{2.5:	'Two	Point	Five',	3:	'+',	'One': 1.35,	7.9:	2}
#Note that items in  a dictionary  are not stored in  the same order as the way you declare them.
	
#print	the	item	with	key	=	“One”.
print(myDict["One"])
#You’ll	get 1.35

#print	the	item	with	key	=	7.9.
print(myDict[7.9])
#You’ll	get	2

#modify	the	item	with	key	=	2.5	and	print	the	updated dictionary
myDict[2.5]	=	"Two and a Half"
print(myDict)
#You’ll	get	{2.5:	'Two	and	a	Half',	3:	'+',	'One': 1.35,	7.9:	2}
	
#add	a	new	item	and	print	the	updated	dictionary
myDict["New item"]	=   "I’m new"
print(myDict)
#You’ll	get	{'New	item':	'I’m	new',	2.5:	'Two	and	a Half',	3:	'+',	'One':	1.35,	7.9:	2}
	
#remove	the	item	with	key	=	“One”	and	print	the updated	dictionary
del	myDict["One"]
print(myDict)
#You’ll	get	{'New	item':	'I’m	new',	2.5:	'Two	and	a Half',	3:	'+',	7.9:	2}
	

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pineapple']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print "It is %d" % number

for fruit in fruits:
    print "%s is a fruit" % fruit 

for i in change:
    print "I've got %r " % i

elements = []
for i in range(0,6):
    print "adding %d to the list " % i
    elements.append(i)

for i in elements:
    print "Elements has %r elements" %i

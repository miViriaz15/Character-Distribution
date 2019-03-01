"""
distribution.py
Author: <miviriaz
Credit: https://www.geeksforgeeks.org/python-sort-list-according-length-elements/

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

words=str(input("Please enter a string of text (the bigger the better): "))
newwords=words.lower()
characterlist=list(newwords)
atoz=string.ascii_lowercase
mylist=[]
for l in characterlist:
    if l in atoz:
        mylist=mylist+list(l)
newlist=mylist.sort()
#print(newlist) 
number=len(newlist)
newestlist=[]
newestlist=list(newlist[0])

for x in range(1, number):
    if newlist[x]==newlist[x-1]:
        newestlist[len(newestlist)-1]=str(newestlist[len(newestlist)-1])+str(newlist[x]) #need to append to element
    else:
        newestlist.append(newlist[x]) #append to list
        
#print(newestlist)
final=sorted(newestlist,reverse=True,key=len)
#print(final)
print('The distribution of characters in "' + words + '" is: ')
for r in final:
    print(r)

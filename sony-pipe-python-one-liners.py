from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Sony's Open Source command-line tool for performing python one-liners using unix-like pipes
They call it "The Pyed Piper" or pyp. It's pretty similar to the -c way of executing python, 
but it imports common modules and has its own preset variable that help with splitting/joining, 
line counter, etc. You use pipes to pass information forward instead of nested parentheses, and 
then use your normal python string and list methods. Here is an example from the homepage:

Here, we take a Linux long listing, capture every other of the 5th through the 10th lines, 
keep the username and filename fields, replace "hello" with "goodbye", capitalize the first 
letter of every word, and then add the text "is splendid" to the end:


ls -l | pyp "pp[5:11:2] | whitespace[2], w[-1] | p.replace('hello','goodbye') | p.title(),'is splendid'"
and the explanation:

This uses pyp's built-in string and list variables (p and pp), as well as the variable whitespace and its shortcut w, which both represent a list based on splitting each line on whitespace (whitespace = w = p.split()). The other functions and selection techniques are all standard Python. Notice the pipes ("|") are inside the pyp command.

http://code.google.com/p/pyp/ http://opensource.imageworks.com/?p=pyp


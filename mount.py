#!/usr/bin/env python
f1 = open("/proc/mounts")#opens file /proc/mounts into f1
rm = f1.readlines()# reads the file line by line
for x in rm[1:]:# for loop which begins from the second line of the file
    sm = x.split(" ")#splits the file line by line according to spaces
    del sm[-2]#deletes the  second last zero from the file
    del sm[-1]#deletes the last zero from the file
    sm.insert(2,"type ")# the string "type" is inserted in index 2
    sm.insert(1,"on")# the string "on" is inserted in index 1
    sm.insert(5,"(")# the opening bracket "(" is inserted in the 5th index
    sm.insert(7,")")# the closing bracket ")" is inserted in the 7th index
    str = " ".join(sm)# the splitted string is joined using the join() function
    print str #the required output is printed and the for loop ends
f1.close()# file f1 is closedi

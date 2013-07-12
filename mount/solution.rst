MOUNT 
-----
Write a file mount.py which when excetued gives the ouput same as that when executing $mount command. This needs to be done using python code .

CODE EXPLANATION
----------------
step 1: open the file /proc/mounts in the default read mode.
step 2: read the file line by line 
step 3: start a loop from the second line of the file
step 4: split the file in order to convert the line of the file from string to list.
step 5: delete the last to 0's in the line
step 6: insert "on" on the 1st position, "type" on the 2nd position and "(" on the 5th and ")" on the 7th position.
step 7: then the splitted string is further joined using the function join()
step 8: for loop ends
step 9: close the file

Link to the code https://github.com/puspita23/puspita_utility/blob/master/mount.py


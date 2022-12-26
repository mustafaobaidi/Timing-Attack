# Timing-Attack

In this script, we attempt to expose a system that uses a vulnerable function in order to verify the login password. It is definetly recommended to stay away from those functions, as they leave a lot of room for threat actors to launch attacks on those functions.

The vulnerable function uses a for loop that would exit the moment a mismatched character 
is found by the function; it also will keep comparing the next character in case of a match 
in the previous one. The main problem here is we can time this function and see when the 
program exits and guess the password character by character. Given that the function 
takes a longer time when a correct match occurs, we can use that to our advantage by 
passing random characters and analyzing which one takes the longest run time. The 
character that took the longest run time to compare with the real password is the correct 
character, we can do this and brute force all the functions to crack the password. An 
implementation of this is provided in the script “timing_attack.py”.


Limitations and assumptions for timing_attack.py:

1-  assuming that the length of the password is given for simplicity.
2- the script only uses lower case letters, (no digits or capital letters).
3-  The script can guess up to a length of 9 charchters.

Note: In order to change the password you can do that by changing 'password.txt' file

To run the script: python timing_attack.py
